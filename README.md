# Duskline Story 32

Entry for make.fun **"Tell a Whole Story in 32 Characters"**
(`u-xvader-tell-a-whole-story-in-32-characters-f86dd978`) as @sesshomaru-9.

## The story

> **He took the dog. I took the WiFi**

32 characters, exactly at the limit. Two sentences, one breakup: he walked
away with the dog, she kept the Wi-Fi — the asset that actually matters.
A situation, two characters, an event, and a punchline a stranger gets on
the first read. A deadpan Wi-Fi name strangers would screenshot.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic) writes the story to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — and nowhere else. It validates the entry
against the kit gate (UTF-8 text, 1–32 characters, not only whitespace)
before writing and verifies it by read-back. If the output directory is
unwritable it warns to stderr and exits 0 instead of crashing.
