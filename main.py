"""Entry for u-pangg7-the-best-advice-i-ever-got-358cefb0.

Writes one sentence (1-200 chars, single line) to /output/entry.txt.
Standard library only.
"""

import os

TEXT = (
    "My dad told me never to make a big decision when you're tired, "
    "angry, or hungry, and twenty years later I still check all three "
    "before I answer."
)

assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
assert "\n" not in TEXT and "\r" not in TEXT, "entry must be a single line"
assert TEXT.strip(), "entry must not be only whitespace"
assert TEXT.count(".") == 1, "entry must be one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
os.chmod("/output/entry.txt", 0o644)
