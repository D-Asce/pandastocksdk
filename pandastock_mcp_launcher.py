"""Console entrypoint: run the pandaData stdio MCP server.

The 22-tool server lives in ``mcp/server.py`` (kept importable both from a
source checkout and from an installed wheel via setuptools data-files). This
launcher locates it, executes it as ``__main__`` and hands stdio over to the
MCPServer loop.
"""
import os
import runpy
import sys
from pathlib import Path


def _server_path() -> Path | None:
    here = Path(__file__).resolve().parent
    candidates = [
        here / "mcp" / "server.py",
        Path(sys.prefix) / "share" / "pandastock-mcp" / "server.py",
        Path(sys.prefix) / "local" / "share" / "pandastock-mcp" / "server.py",
    ]
    return next((p for p in candidates if p.exists()), None)


def main() -> None:
    server = _server_path()
    if server is None:
        sys.exit(
            "pandaData MCP server.py not found (expected in source tree "
            "mcp/server.py or installed share/pandastock-mcp/server.py)."
        )
    sys.argv[0] = str(server)
    runpy.run_path(str(server), run_name="__main__")


if __name__ == "__main__":
    main()