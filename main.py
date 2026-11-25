#!/usr/bin/env python3
"""Write the phone's last words at 1 percent to entry.txt.

Entry for make.fun's "Famous Last Words at 1 Percent" bounty. The
program writes exactly one line of text and nothing else.

How the line targets the brief: the entry is a dying phone's farewell,
structured like a deathbed will -- a message for the charger it loved,
one for the group chat it dies inside mid-sentence, and a final jab at
the owner who ignored the power bank sitting right there. The last
clause is the turn: the phone dies vindicated, not helpless.
"""

import os
from pathlib import Path

LINE = "Tell the charger I always loved it, tell the group chat I died mid-sentence, and tell my owner the power bank was right there."

MAX_CHARS = 199
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 199 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
