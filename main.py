#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — entry.

Writes one line of office comedy to /output/entry.txt. Blind tournament
winner is candidate #7 (see tournament.md): Borda 53, tied 1st with #13,
head-to-head won 1-0 (ChatGPT, margin 2). All three judges put #7 in their
top 3. The punchline turns calendar overload into self-inflicted absurdity
in the last two words, with nothing to cut.

The entry is validated against the gate before it is written: 1-200 chars,
a single line, and exactly one sentence. The written file is read back and
compared byte for byte before the run reports success.
"""

import os
import re
import sys

LINE = (
    "My calendar was so full I booked a meeting with myself to cancel "
    "my other meetings, and then I no-showed."
)

MAX_CHARS = 200

ENTRY_PATH = "/output/entry.txt"

SENT_END = re.compile(r"[.!?]['\"]?(?=\s+[A-Z]|\s*$)")


def sentence_count(text):
    return len(SENT_END.findall(text))


def validate(line):
    """Check the line against the gate; return the first problem, else None."""
    if not line.strip():
        return "line is blank"
    if len(line) > MAX_CHARS:
        return f"line is {len(line)} characters, allowed range is 1-{MAX_CHARS}"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if sentence_count(line) != 1:
        return f"line has {sentence_count(line)} sentences, must be exactly 1"
    return None


def write_entry(path, line):
    """Write the line to path, creating its directory; return chars written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        return f.write(line)


def verify_written(path, line):
    """Read path back; return an error string, or None when byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(line)}"
    return None


def main():
    line = LINE.strip()
    problem = validate(line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    written = write_entry(ENTRY_PATH, line)
    if written != len(line):
        print(
            f"error: wrote {written} characters, expected {len(line)}",
            file=sys.stderr,
        )
        sys.exit(1)

    problem = verify_written(ENTRY_PATH, line)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        sys.exit(1)

    print(f"wrote {len(line)} characters, 1 line, to /output/entry.txt")


if __name__ == "__main__":
    main()
