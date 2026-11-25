#!/usr/bin/env python3
"""Duskline Story 32 — Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name of at most 32 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The story: "He took the dog. I took the WiFi"
Two sentences, one breakup: he walked away with the dog, she kept the
Wi-Fi — the asset that actually matters. A situation, two characters,
an event, and a punchline a stranger gets on the first read, in exactly
32 characters.

Deterministic, Python 3.13 stdlib only. Writes ONLY to
$MAKEFUN_OUTPUT_DIR (never to the repo directory). Validates the entry
against the kit gate before writing and verifies it by read-back.
Never crashes if the output dir is unwritable: warns to stderr, exits 0.
"""

import os
import sys

STORY = "He took the dog. I took the WiFi"
GATE_FILE = "entry.txt"
MAX_CHARS = 32


def _validate_entry(text: str) -> None:
    """Gate check matching the kit: UTF-8 text, 1-32 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    try:
        _validate_entry(STORY)
    except ValueError as exc:
        print(f"gate failed: {exc}", file=sys.stderr)
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR not set; nothing to write", file=sys.stderr)
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, GATE_FILE)
        # No trailing newline: the file is exactly the 32-character story.
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(STORY)
        with open(path, "r", encoding="utf-8", newline="") as fh:
            written = fh.read()
        _validate_entry(written)
        if written != STORY:
            print("read-back mismatch", file=sys.stderr)
            return 0
    except OSError as exc:
        print(f"cannot write output ({exc}); skipping", file=sys.stderr)
        return 0
    except ValueError as exc:
        print(f"read-back gate failed: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
