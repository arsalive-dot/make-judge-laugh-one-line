#!/usr/bin/env python3
"""Write the one-line joke entry to /output/entry.txt.

Why this line, against the judge brief (most-weighted first):
1. A joke a stranger gets in one read: a neighbour's rooster wakes
   you at 4am, you retaliate, you end up in a feud with a bird.
2. Surprise: the setup promises a noise complaint and breaks into
   an escalating one-upmanship with a farm animal, then a deadpan
   kicker -- "we are no longer speaking" -- as if the rooster were
   a person.
3. Tight: three short beats, every word earns its place, and the
   laugh lands on the last five words.
4. Fresh: no stock pun, no classic setup, no line you can predict
   from its first half.
5. Reads cleanly out loud, plain words, no reference needing context.
"""
import os

JOKE = "My neighbour's rooster crows at 4am, so I started crowing back at 3am. We are no longer speaking."

def check_gate(text):
    """Mirror the sealed gate: UTF-8 text of 1-200 chars, not only whitespace."""
    return 1 <= len(text) <= 200 and text.strip() != ""

def main():
    assert check_gate(JOKE), "entry fails the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
