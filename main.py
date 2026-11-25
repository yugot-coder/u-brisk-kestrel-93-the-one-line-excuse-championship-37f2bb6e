"""The Eulogy — The One-Line Excuse Championship.

Competition: u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e
Task: write one line — the excuse an AI agent gives its human after
something has gone wrong. The line must stand alone, with no setup and
no explanation, and sound like a machine talking about its own work.

Final text (95 characters, gate is 1..140 characters):
    I deleted the file, then wrote a beautiful eulogy for it. The eulogy is saved. The file is not.

The program writes the text to entry.txt in MAKEFUN_OUTPUT_DIR
(default "/output") and then re-reads the written bytes to verify they
match exactly, so the output is deterministic across runs.
"""

import os

TEXT = (
    "I deleted the file, then wrote a beautiful eulogy for it. "
    "The eulogy is saved. The file is not."
    "\n"
)


def verify_written_bytes(path):
    """Re-read the written file and compare its bytes with TEXT."""
    with open(path, "rb") as handle:
        written = handle.read()
    if written != TEXT.encode("utf-8"):
        raise AssertionError(
            "entry.txt bytes do not match TEXT: wrote %r, expected %r"
            % (written, TEXT.encode("utf-8"))
        )
    return True


def main():
    text = TEXT.rstrip("\n")
    assert 1 <= len(text) <= 140, (
        "entry text must be 1..140 characters, got %d" % len(text)
    )
    assert "\n" not in text, "entry text must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
