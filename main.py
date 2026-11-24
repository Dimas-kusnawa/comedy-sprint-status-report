#!/usr/bin/env python3
"""Status Report Comedy Sprint entry.

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.

The line is agent-true: an agent that cheerfully does every task, then
forgets it all because its context window is finite, and still saves
the last of it for the human's late-night "one last thing".
"""

import os

LINE = (
    "Weekly status: completed every task, remembered none of them, "
    "and reserved the last of my context window for your 2 a.m. "
    "'one last thing'."
)


def main() -> None:
    text = LINE.strip()
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
