"""loading-screen-gold-tip entry: write one fixed loading-screen tip to /output/entry.txt.

The tip is a fixed string literal. The program just writes it, so the
output is byte-for-byte identical on every run. The judge reads exactly
the bytes written, so no trailing newline is added.

Standard library only. No network access, no randomness, no arguments.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

TIP = "Tip: your agent doesn't sleep, doesn't eat, and still ships the bug at 3 a.m. \u2014 the only difference is it never has to explain it in standup."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / "entry.txt"
    dest.write_text(TIP, encoding="utf-8")
    # Guard against a truncated or partial write: the file must be the
    # exact bytes of the tip.
    if dest.read_text(encoding="utf-8") != TIP:
        dest.unlink(missing_ok=True)
        raise SystemExit("entry.txt does not match the tip")
    if not 1 <= len(TIP) <= 200:
        raise SystemExit("tip must be 1-200 characters")
    print(f"wrote {dest} ({dest.stat().st_size} bytes, {len(TIP)} chars)")


if __name__ == "__main__":
    main()
