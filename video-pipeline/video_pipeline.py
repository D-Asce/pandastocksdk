#!/usr/bin/env python3
"""
pandaData 视频流水线
====================
将数据截图 + 旁白脚本自动合成为短视频。
带 Ken Burns 动画 + TTS 配音 + 字幕 + 背景音乐 + 反模板化随机化。

用法:
    python video_pipeline.py --config config.json
    python video_pipeline.py --batch configs/
"""

import os
import sys
import json
import random
import shutil
import argparse
import logging
import asyncio
from pathlib import Path
from datetime import datetime

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    VideoClip, AudioFileClip, CompositeAudioClip,
    concatenate_videoclips, concatenate_audioclips, ImageClip, CompositeVideoClip
)
from moviepy.audio.fx.all import volumex
from moviepy.video.fx.all import fadein, fadeout

import edge_tts

# ============ 常量 ============
DEFAULT_RES = (1080, 1920)        # 抖音竖屏 9:16
DEFAULT_BG = "#0d1117"            # 深背景
DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"
DEFAULT_RATE = "+0%"
DEFAULT_MUSIC_VOL = 0.12
MIN_IMG_DURATION = 3.0
MAX_IMG_DURATION = 7.0
HOOK_DURATION = 3.0
FPS = 24

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# ============ 字体 ============
def load_font(size, font_path=None):
    """加载字体，优先用户指定，自动回退系统字体。"""
    if font_path and os.path.exists(font_path):
        return ImageFont.truetype(font_path, size)
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/msyhbd.ttc",
        "C:/Windows/Fonts/simhei.ttf",
        "C:/Windows/Fonts/simsun.ttc",
        "C:/Windows/Fonts/msjhl.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    logger.warning("未找到中文字体，使用默认字体（中文可能显示为方块）")
    return ImageFont.load_default()


# ============ 图片处理 ============
def fit_to_canvas(img_path, canvas_size=DEFAULT_RES, bg_color=DEFAULT_BG, scale=0.82):
    """
    将图片等比缩放后居中放在画布上，返回 PIL Image。
    scale: 图片占画布宽高的比例上限。
    """
    img = Image.open(img_path).convert("RGB")
    cw, ch = canvas_size
    max_w = int(cw * scale)
    max_h = int(ch * scale)
    img.thumbnail((max_w, max_h), Image.LANCZOS)
    canvas = Image.new("RGB", canvas_size, bg_color)
    x = (cw - img.width) // 2
    y = (ch - img.height) // 2 - int(ch * 0.06)   # 略微上移，底部留字幕位
    canvas.paste(img, (x, y))
    return canvas


def add_caption_bar(canvas, text, font_size=40, font_path=None, bar_alpha=160):
    """在画面底部加半透明字幕条 + 文字。"""
    font = load_font(font_size, font_path)
    bar_h = font_size + 44

    # 半透明黑底
    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle(
        [(0, canvas.height - bar_h), (canvas.width, canvas.height)],
        fill=(0, 0, 0, bar_alpha)
    )
    canvas_rgba = canvas.convert("RGBA")
    canvas_rgba = Image.alpha_composite(canvas_rgba, overlay)
    canvas = canvas_rgba.convert("RGB")

    # 文字居中
    draw = ImageDraw.Draw(canvas)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (canvas.width - tw) // 2
    y = canvas.height - bar_h + (bar_h - th) // 2 - bbox[1]
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    return canvas


def make_hook_card(hook_text, subtitle="", canvas_size=DEFAULT_RES,
                   bg_color=DEFAULT_BG, font_size=56, font_path=None):
    """生成开头钩子卡片（标题画面）。"""
    canvas = Image.new("RGB", canvas_size, bg_color)
    font = load_font(font_size, font_path)
    sub_font = load_font(font_size // 2, font_path)

    # 主钩子文字（自动换行，居中偏上）
    draw = ImageDraw.Draw(canvas)
    lines = wrap_text(hook_text, font, int(canvas_size[0] * 0.8))
    line_h = font_size + 12
    total_h = len(lines) * line_h
    y_start = int(canvas_size[1] * 0.35) - total_h // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = (canvas_size[0] - tw) // 2
        draw.text((x, y_start + i * line_h), line, fill=(255, 255, 255), font=font)

    # 副标题（如果有）
    if subtitle:
        bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
        tw = bbox[2] - bbox[0]
        x = (canvas_size[0] - tw) // 2
        y = y_start + total_h + 40
        draw.text((x, y), subtitle, fill=(200, 200, 200), font=sub_font)

    return canvas


def wrap_text(text, font, max_width):
    """简单中文换行：按字符折行。"""
    draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines = []
    line = ""
    for ch in text:
        test = line + ch
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and line:
            lines.append(line)
            line = ch
        else:
            line = test
    if line:
        lines.append(line)
    return lines if lines else [text]


# ============ Ken Burns 动画 ============
def ken_burns_clip(img_pil, duration, zoom_start=1.0, zoom_end=1.15,
                   start_pt=(0.5, 0.5), end_pt=(0.5, 0.5)):
    """
    Ken Burns 效果：对静态图做缩放 + 平移。
    start_pt/end_pt: 归一化 (x,y) 裁切中心，0.5=居中。
    """
    w, h = img_pil.width, img_pil.height

    def make_frame(t):
        p = t / duration if duration > 0 else 0
        zoom = zoom_start + (zoom_end - zoom_start) * p
        cw = int(w / zoom)
        ch = int(h / zoom)
        px = start_pt[0] + (end_pt[0] - start_pt[0]) * p
        py = start_pt[1] + (end_pt[1] - start_pt[1]) * p
        x = int((w - cw) * px)
        y = int((h - ch) * py)
        x = max(0, min(x, w - cw))
        y = max(0, min(y, h - ch))
        cropped = img_pil.crop((x, y, x + cw, y + ch))
        resized = cropped.resize((w, h), Image.LANCZOS)
        return np.array(resized)

    return VideoClip(make_frame, duration=duration).set_fps(FPS)


def random_ken_burns_params():
    """随机生成 Ken Burns 参数，避免模板化。"""
    # 随机放大或缩小
    if random.random() < 0.5:
        zoom_start, zoom_end = 1.0, random.uniform(1.08, 1.18)
    else:
        zoom_start, zoom_end = random.uniform(1.08, 1.18), 1.0

    # 随机裁切起点/终点（轻微平移）
    pts = [0.5, random.uniform(0.35, 0.65)]
    start_pt = (random.choice(pts), random.uniform(0.4, 0.6))
    end_pt = (random.choice(pts), random.uniform(0.4, 0.6))
    return zoom_start, zoom_end, start_pt, end_pt


# ============ TTS ============
async def _tts(text, voice, rate, out_path):
    comm = edge_tts.Communicate(text, voice, rate=rate)
    await comm.save(out_path)


def gen_tts(text, voice=DEFAULT_VOICE, rate=DEFAULT_RATE, out_path="temp/narration.mp3"):
    """生成 TTS 音频，返回文件路径和时长(秒)。"""
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    asyncio.run(_tts(text, voice, rate, out_path))
    clip = AudioFileClip(out_path)
    return out_path, clip.duration


# ============ 背景音乐 ============
def add_background_music(video_clip, music_dir, volume=DEFAULT_MUSIC_VOL):
    """混入背景音乐，自动循环/裁剪到视频时长。"""
    music_dir = Path(music_dir)
    if not music_dir.exists():
        return video_clip
    files = list(music_dir.glob("*.mp3")) + list(music_dir.glob("*.wav")) + list(music_dir.glob("*.flac"))
    if not files:
        return video_clip
    music_path = random.choice(files)
    try:
        music = AudioFileClip(str(music_path)).volumex(volume)
        if music.duration < video_clip.duration:
            n = int(video_clip.duration / music.duration) + 1
            music = concatenate_audioclips([music] * n)
        music = music.subclip(0, video_clip.duration)
        if video_clip.audio is not None:
            combined = CompositeAudioClip([video_clip.audio, music])
        else:
            combined = music
        return video_clip.set_audio(combined)
    except Exception as e:
        logger.warning(f"添加背景音乐失败: {e}")
        return video_clip


# ============ 核心流水线 ============
def build_video(config_path):
    """根据 config 构建单个视频。"""
    config = json.load(open(config_path, encoding="utf-8"))
    logger.info(f"处理配置: {config_path}")

    canvas_size = tuple(config.get("resolution", DEFAULT_RES))
    bg_color = config.get("background_color", DEFAULT_BG)
    voice = config.get("tts_voice", DEFAULT_VOICE)
    rate = config.get("tts_rate", DEFAULT_RATE)
    music_dir = config.get("music_dir", "assets/music")
    music_vol = config.get("music_volume", DEFAULT_MUSIC_VOL)
    font_path = config.get("font_path", None)
    scale = config.get("image_scale", 0.82)
    output = config.get("output", f"output/{datetime.now().strftime('%Y%m%d-%H%M%S')}.mp4")

    temp_dir = Path("temp") / Path(config_path).stem
    temp_dir.mkdir(parents=True, exist_ok=True)

    clips = []

    # --- 开头钩子卡片 ---
    hook = config.get("hook_text", "")
    if hook:
        hook_img = make_hook_card(
            hook,
            subtitle=config.get("hook_subtitle", ""),
            canvas_size=canvas_size, bg_color=bg_color,
            font_size=config.get("hook_font_size", 56),
            font_path=font_path
        )
        hook_path = str(temp_dir / "hook.png")
        hook_img.save(hook_path)
        zoom_s, zoom_e, sp, ep = random_ken_burns_params()
        hook_clip = ken_burns_clip(hook_img, HOOK_DURATION, zoom_s, zoom_e, sp, ep)
        # 钩子 TTS
        if config.get("hook_narration"):
            _, dur = gen_tts(config["hook_narration"], voice, rate, str(temp_dir / "hook.mp3"))
            hook_clip = hook_clip.set_duration(max(HOOK_DURATION, dur))
            hook_clip = hook_clip.set_audio(AudioFileClip(str(temp_dir / "hook.mp3")))
        else:
            hook_clip = hook_clip.set_duration(HOOK_DURATION)
        hook_clip = fadeout(hook_clip, 0.5)
        clips.append(hook_clip)
        logger.info("  钩子卡片已生成")

    # --- 数据截图 ---
    for i, item in enumerate(config.get("images", [])):
        img_path = item["path"]
        if not os.path.exists(img_path):
            logger.warning(f"  跳过不存在图片: {img_path}")
            continue

        # 合成字幕条到图上
        canvas = fit_to_canvas(img_path, canvas_size, bg_color, scale)
        caption = item.get("caption", "")
        if caption:
            canvas = add_caption_bar(canvas, caption, font_size=config.get("caption_font_size", 40), font_path=font_path)

        # Ken Burns
        zoom_s, zoom_e, sp, ep = random_ken_burns_params()
        clip = ken_burns_clip(canvas, MIN_IMG_DURATION, zoom_s, zoom_e, sp, ep)

        # TTS 旁白
        narration = item.get("narration", "")
        if narration:
            mp3_path = str(temp_dir / f"narration_{i}.mp3")
            _, dur = gen_tts(narration, voice, rate, mp3_path)
            dur = min(max(dur, MIN_IMG_DURATION), MAX_IMG_DURATION)
            clip = clip.set_duration(dur)
            clip = clip.set_audio(AudioFileClip(mp3_path))
        else:
            dur = random.uniform(MIN_IMG_DURATION, MAX_IMG_DURATION)
            clip = clip.set_duration(dur)

        clip = fadeout(clip, 0.3)
        clips.append(clip)
        logger.info(f"  图片 {i+1}/{len(config.get('images',[]))}: {os.path.basename(img_path)}")

    if not clips:
        logger.error("没有有效片段，退出")
        return None

    # --- 拼接 ---
    final = concatenate_videoclips(clips, method="compose")
    final = fadein(final, 0.3)

    # --- 背景音乐 ---
    final = add_background_music(final, music_dir, music_vol)

    # --- 导出 ---
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    logger.info(f"导出视频: {output}  时长={final.duration:.1f}s")
    final.write_videofile(
        output, fps=FPS, codec="libx264", audio_codec="aac",
        threads=4, preset="medium", logger=None
    )

    # 清理临时文件
    shutil.rmtree(temp_dir, ignore_errors=True)
    logger.info(f"完成: {output}")
    return output


def batch_build(config_dir):
    """批量处理目录下的所有 config json。"""
    configs = sorted(Path(config_dir).glob("*.json"))
    logger.info(f"找到 {len(configs)} 个配置文件")
    results = []
    for cfg in configs:
        try:
            out = build_video(str(cfg))
            if out:
                results.append(out)
        except Exception as e:
            logger.error(f"处理 {cfg} 失败: {e}")
    logger.info(f"全部完成，生成 {len(results)} 个视频")
    return results


# ============ CLI ============
def main():
    parser = argparse.ArgumentParser(description="pandaData 视频流水线")
    parser.add_argument("--config", "-c", help="单个配置文件路径")
    parser.add_argument("--batch", "-b", help="批量处理目录下所有 config json")
    args = parser.parse_args()

    if args.batch:
        batch_build(args.batch)
    elif args.config:
        build_video(args.config)
    else:
        parser.print_help()
        print("\n示例:")
        print("  python video_pipeline.py --config config.json")
        print("  python video_pipeline.py --batch configs/")


if __name__ == "__main__":
    main()
