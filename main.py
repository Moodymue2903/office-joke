#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — entry.

Writes one line of office comedy to /output/entry.txt. Blind tournament
winner is candidate #7 (see tournament.md): Borda 53, tied 1st with #13,
head-to-head won 1-0 (ChatGPT, margin 2). All three judges put #7 in their
top 3. The punchline turns calendar overload into self-inflicted absurdity
in the last two words, with nothing to cut.
"""

import os
import sys

LINE = (
    "My calendar was so full I booked a meeting with myself to cancel "
    "my other meetings, and then I no-showed."
)

MAX_CHARS = 200


def validate(line):
    """Check the line against the gate: 1-200 chars, single line, non-blank."""
    if not line.strip():
        return "line is blank"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} characters, allowed range is 1-{MAX_CHARS}"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    return None


def main():
    line = LINE.strip()
    problem = validate(line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)

    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        print(
            f"error: read back {len(back)} bytes, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"wrote {len(line)} characters, 1 line, to /output/entry.txt")


if __name__ == "__main__":
    main()
