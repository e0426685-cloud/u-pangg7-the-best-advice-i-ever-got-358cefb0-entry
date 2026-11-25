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

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Check the entry is one sentence of 1-200 chars on a single line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1:
        raise ValueError("entry must be one sentence")
    return True


def main():
    validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
