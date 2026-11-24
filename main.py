"""One Word for Your Wi-Fi — entry program.

Writes one word (<=20 chars) describing Wi-Fi to /output/entry.txt.
Stdlib only, deterministic.
"""
import os

MAX_CHARS = 20  # sealed scorer gate (RULES.txt): 1-20 characters.

TEXT = "Ghosting"


def check_gate(text):
    """Enforce the scorer's gate (RULES.txt): UTF-8 text of 1-20 chars,
    not whitespace-only, no control characters, a single word.
    Fail loudly instead of writing an invalid entry.
    """
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(c) < 32 for c in text):
        return False
    if text.split() != [text] or not text.isalpha():
        return False
    return True


def main():
    if not check_gate(TEXT):
        raise SystemExit("entry text violates the 1-20 char single-word gate")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Write-verify: read the file back and refuse to exit cleanly if
    # the bytes on disk differ from the gated text.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise SystemExit("entry.txt on disk does not match the gated text")


if __name__ == "__main__":
    main()
