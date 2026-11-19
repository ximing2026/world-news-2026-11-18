"""One-day news poster entry: copies the committed poster image to the output.

The image (entry.png, beside this file) sums up the world news of
Wednesday 18 November 2026 as a newspaper front page. The grader runs
this program twice with no network, and both runs must write the same
bytes, so the program does a plain byte-for-byte copy of a file that
never changes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    data = SOURCE.read_bytes()
    if len(data) > 1_048_576 or not data.startswith(b"\x89PNG"):
        raise SystemExit("entry.png missing or not a PNG within the size cap")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
