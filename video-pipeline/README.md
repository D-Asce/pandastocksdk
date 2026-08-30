# pandaData 视频流水线

将数据截图 + 旁白脚本自动合成为短视频，一键生成可发抖音/视频号/小红书的内容。

## 特性

- **Ken Burns 动画**：每张图自动加缩放/平移，避免静止低质
- **TTS 配音**：基于 edge-tss 免费中文音色，自动生成旁白
- **字幕条**：底部半透明字幕，说明数据维度
- **背景音乐**：自动混入 BGM，循环/裁剪到视频时长
- **开头钩子**：支持标题卡片 + 钩子话术，前3秒抓人
- **反模板化**：随机缩放方向、平移路径、背景音乐，避免被判"模板低质"
- **批量模式**：一个目录丢多个 config，批量出片

## 安装

```bash
# 1. 安装 ffmpeg（moviepy 依赖）
# Windows: choco install ffmpeg   或  从 https://ffmpeg.org 下载
# macOS:   brew install ffmpeg
# Linux:   sudo apt install ffmpeg

# 2. 安装 Python 依赖
cd video-pipeline
pip install -r requirements.txt
```

## 快速开始

### 1. 准备截图
把你工具输出的图表放进 `input/`，例如：
```
input/资金流/01-概览.png
input/资金流/02-排行.png
```

### 2. 写配置文件
复制 `config.example.json` 改名为 `config.json`，填入图片路径和旁白文字。

旁白文字即 TTS 配音内容，按"合规框架"写：
- 只展示数据能力，不说"买/卖/荐股"
- 结尾挂"数据仅供参考，不构成投资建议"

### 3. 生成视频
```bash
python video_pipeline.py --config config.json
```
输出在 `output/` 目录。

### 4. 批量生成
```bash
python video_pipeline.py --batch configs/
```

## 配置字段

| 字段 | 说明 | 默认 |
|---|---|---|
| `hook_text` | 开头钩子大标题 | - |
| `hook_subtitle` | 钩子副标题 | - |
| `hook_narration` | 钩子旁白（TTS） | - |
| `resolution` | 分辨率 | [1080,1920] 竖屏 |
| `background_color` | 背景色 | #0d1117 |
| `tts_voice` | 音色 | zh-CN-XiaoxiaoNeural |
| `tts_rate` | 语速 | +0% |
| `music_dir` | 背景音乐目录 | assets/music |
| `music_volume` | BGM 音量 | 0.12 |
| `images` | 截图列表（path/caption/narration） | - |
| `output` | 输出路径 | output/时间戳.mp4 |

## TTS 音色推荐

- `zh-CN-XiaoxiaoNeural` 女声自然（默认）
- `zh-CN-YunxiNeural` 男声活力
- `zh-CN-YunjianNeural` 男声沉稳
- `zh-CN-XiaoyiNeural` 女声温柔

## 合规注意

视频内容请始终定位为 **数据工具演示 / 编程教学**：
- ✅ 展示"工具能输出什么数据"
- ✅ 讲"怎么用代码取数"
- ❌ 不说"买XX股票"
- ❌ 不晒收益、不承诺回报
- 简介挂："仅供数据学习，不构成投资建议"

## 目录结构

```
video-pipeline/
├── video_pipeline.py          # 主脚本
├── requirements.txt           # 依赖
├── config.example.json        # 配置示例
├── input/                     # 放截图
│   └── 资金流/
├── assets/music/              # 放背景音乐 .mp3
├── output/                    # 生成的视频
├── temp/                      # 临时文件（自动清理）
└── configs/                   # 批量模式配置目录
```
