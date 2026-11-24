#!/usr/bin/env python3
"""The One-Line Exit — account B (Slothana / keen-panda-72).

Writes one funny one-line resignation letter to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), for make.fun competition
u-kreutzx-the-one-line-exit-1dc652d1 ("The One-Line Exit", $2 total).

The gate: entry.txt must be UTF-8 text of 1 to 140 characters, not only
white space, a single line, printable, ending in terminal punctuation.
"""

import os
import sys

# The sealed gate caps the entry at 140 characters (RULES.txt: "1 to 140
# characters"). Keep the line comfortably inside that cap.
MAX_LEN = 140
TERMINAL_PUNCTUATION = ".!?"


def build_line() -> str:
    """Return the one-line resignation letter.

    Voice: a lighthouse keeper (specific job, specific workplace).
    Turn: twelve years spent warning ships *away* from the rocks, and the
    resignation is to go and meet the rocks — the job's whole purpose,
    inverted, in the final clause. Reads as a letter someone could send.
    """
    return (
        "I hereby resign as lighthouse keeper \u2014 after twelve years of "
        "warning ships away from the rocks, I've decided to go and meet them."
    )


def validate(line: str) -> str:
    """Check the line against the kit gate; raise ValueError if it fails."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) < 1 or len(line) > MAX_LEN:
        raise ValueError(
            f"entry must be 1 to {MAX_LEN} characters, got {len(line)}"
        )
    if not line.isprintable():
        raise ValueError("entry must be printable text")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if line[-1] not in TERMINAL_PUNCTUATION:
        raise ValueError("entry must end in terminal punctuation (. ! ?)")
    if "resign" not in line.lower():
        raise ValueError("entry must read as a resignation letter")
    return line


def write_entry(line: str, out_dir: str | None = None) -> str:
    """Validate the line and write it to <out_dir>/entry.txt."""
    validate(line)
    out_dir = out_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> int:
    line = build_line()
    path = write_entry(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
