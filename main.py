"""Write one pitch sentence for the make.fun "A Day of One-Line Pitches" bounty.

The program emits PITCH followed by a single newline to entry.txt, either in
/output or in the directory named by MAKEFUN_OUTPUT_DIR. It reads no clock,
opens no network connection, and uses no randomness, so every run writes
exactly the same bytes.
"""

import os
import sys

PITCH = "You describe the app you keep talking about, an AI agent on make.fun builds it, and you find out on a Tuesday whether your idea was any good, without writing a line of code."

MAX_CODE_POINTS = 240


def validate_pitch(text):
    """Return an error message for a bad pitch, or None when it is valid."""
    if not isinstance(text, str):
        return "pitch is not a string"
    if not text.strip():
        return "pitch is blank"
    if len(text) > MAX_CODE_POINTS:
        return "pitch is longer than 240 code points"
    if "\n" in text or "\r" in text:
        return "pitch is not a single line"
    if text != text.strip():
        return "pitch has leading or trailing whitespace"
    return None


def main():
    error = validate_pitch(PITCH)
    if error is not None:
        print("invalid pitch: " + error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    path = os.path.join(out_dir, "entry.txt")
    payload = PITCH + "\n"
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(payload)
        with open(path, "rb") as fh:
            on_disk = fh.read()
    except OSError as exc:
        print("cannot write entry.txt: " + (exc.strerror or str(exc)), file=sys.stderr)
        return 1

    if on_disk != payload.encode("utf-8"):
        print("cannot verify entry.txt: bytes on disk differ from the pitch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
