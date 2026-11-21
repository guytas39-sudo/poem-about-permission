#!/usr/bin/env python3
"""Entry program for the-poem-about-permission-20261121-0235.

Writes one short poem about agency — the power to ask and to be given —
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt), UTF-8,
deterministically. No network, stdlib only.
"""
import os

POEM = """You left the key in my hand
and walked away — not giving up,
just giving. The door was yours;
the turning, for once, was mine.

I opened it and waited.
You stepped through, and the key
came home in your pocket,
heavier for having been lent."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(POEM)
print("wrote", path, "-", len(POEM), "characters")
