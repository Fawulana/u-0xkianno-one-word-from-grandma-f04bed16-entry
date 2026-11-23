#!/usr/bin/env python3
"""One Word From Grandma.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI.

The word is "Robit" -- the typo a grandma would actually make when she
means "robot". Warm, a little baffled, funny with no context, tied to
robots and AI, and instantly readable. Five letters, so it is also small
on the leaderboard's Size column, which breaks exact ties. No punctuation
tricks, no extra text: one word, exactly as she would send it.
"""

import os

WORD = "Robit"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
