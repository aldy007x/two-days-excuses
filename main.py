#!/usr/bin/env python3
"""Two Days of Excuses — make.fun bounty entry.

Writes a single original one-line excuse, in the voice of an AI agent,
for a missed deadline. Deterministic: no network, no randomness, and
no external input — the line is embedded below as a constant.
"""

import os
import sys

# The entry: the joke is the gap between the machine's total
# confidence (99.9%) and its total failure to act at all.
ENTRY = "I was 99.9% confident I'd finish on time, so I never actually started."


def main() -> int:
    # Self-check: exactly one non-blank line, 1-200 characters,
    # with no leading/trailing whitespace padding the count.
    lines = ENTRY.splitlines()
    if (
        len(lines) != 1
        or not ENTRY.strip()
        or ENTRY != ENTRY.strip()
        or not 1 <= len(ENTRY) <= 200
    ):
        print(
            f"error: entry must be exactly one non-blank line of 1-200 "
            f"characters, got {len(ENTRY)} characters",
            file=sys.stderr,
        )
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(f"Wrote entry ({len(ENTRY)} characters) to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
