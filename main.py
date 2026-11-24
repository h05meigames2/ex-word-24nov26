#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. Python standard library only, no network,
fully deterministic.
"""

import os

WORD = "noncommittal"


def main() -> None:
    # Gate check: exactly one word, 1-24 characters, letters only.
    assert WORD.isalpha() and 1 <= len(WORD) <= 24, WORD
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
