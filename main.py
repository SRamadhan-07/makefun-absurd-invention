#!/usr/bin/env python3
"""Entry for make.fun's "One-Sentence Absurd Invention Pitch".

Writes a single sentence to /output/entry.txt: a pitch for the Apology
Toaster, a ridiculous invention that fixes the tiny everyday annoyance
of burnt breakfast. Standard library only; no network.
"""

import os

# The whole entry is this one sentence (157 characters, inside the
# competition's gate of 1 to 220 characters).
PITCH = (
    "Introducing the Apology Toaster: every time it burns your breakfast, "
    "it browns the word 'sorry' onto the next slice, so at least the bad "
    "news arrives edible."
)


def check_pitch(text: str) -> None:
    """Guard the gate: exactly one sentence of 1 to 220 characters."""
    if not 1 <= len(text) <= 220:
        raise ValueError("pitch is outside the 1-220 character gate")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be a single sentence")


def main() -> None:
    check_pitch(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the sentence and nothing else.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PITCH)


if __name__ == "__main__":
    main()
