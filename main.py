"""Midnight Fridge Roast: one-line roast of a smart fridge.

Writes a single original one-line roast to /output/entry.txt.
Deterministic: no clock, no randomness, no network, no model calls.
The line is 90 characters, one line, inside the 1-200 gate.
"""

import os
from pathlib import Path

SETUP = "My smart fridge locks at midnight"
BEAT = "\u2014"
PUNCH = "the leftovers took out a restraining order against me."


def build_roast() -> str:
    """Assemble the single roast line from its parts.

    Setup names the fridge's petty rule itself (it locks at midnight);
    the punch turns the fridge's refusal into the leftovers taking
    legal action against the hungry owner, so the laugh comes from
    the rule, not from generic smart-home grumbling. One line, tight,
    the kind of thing a person would actually say out loud at the
    fridge door at 12:01.
    """
    return f"{SETUP} {BEAT} {PUNCH}"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = (output_dir / "entry.txt").resolve()
    # Refuse to write outside the intended output directory.
    if output_path.parent != output_dir.resolve():
        raise ValueError("unsafe output path")
    line = build_roast()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"roast line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    # Write exactly the roast line: no trailing newline, so the file
    # holds one line of 1-200 characters and nothing else.
    output_path.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
