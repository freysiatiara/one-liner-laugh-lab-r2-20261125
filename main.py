#!/usr/bin/env python3
"""One-Liner Laugh Lab, round 2: the vacuum's excuse for eating a sock.

The program's only job is to deliver one fixed funny line, byte-identically
on every run, to ``entry.txt`` in the grader's output directory. The line
answers the prompt -- the excuse a robot vacuum gives after eating a sock --
with a two-beat joke: a mistaken-identity confession, then an absurd
escalation (the "victim" files a formal complaint).

The gate allows UTF-8 text of 1 to 200 characters with no trailing newline,
so the line is written exactly as-is: no newline, no extra whitespace.

Standard library only. No network, no input files, no randomness.
"""

import os

LINE = "I mistook it for a very flat cat. The cat has since filed a complaint."
OUTPUT_NAME = "entry.txt"


def output_dir() -> str:
    """Grader output directory: $MAKEFUN_OUTPUT_DIR, else /output."""
    configured = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if configured:
        return configured
    return "/output"


def main() -> None:
    # Guard the sealed gate up front: the entry must be 1-200 UTF-8
    # characters and more than whitespace, or the judge never sees it.
    text = LINE
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry line fails the 1-200 character gate")
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
