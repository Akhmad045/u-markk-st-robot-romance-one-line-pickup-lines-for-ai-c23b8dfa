#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

Writes the entry line to /output/entry.txt (UTF-8, no trailing newline),
then read-checks the file it wrote. The gate requires 1-200 characters,
not only whitespace, on a single line.

Run:
    python3 main.py              # write /output/entry.txt
    python3 main.py --self-test  # validate the gate and the written file
"""

import os
import sys

LINE = "Call me a language model, because the only thing I can predict next is you."

OUTPUT_PATH = "/output/entry.txt"


def valid(text):
    """The gate, as the kit states it: 1-200 UTF-8 characters, not only
    whitespace, on one line, with no control characters and no leading or
    trailing whitespace."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False
    # Reject invisible Unicode format characters that would smuggle a
    # second line or hidden content past a reader.
    if any(0x200B <= ord(ch) <= 0x200F or ord(ch) in (0xFEFF, 0x2060)
           for ch in text):
        return False
    return True


def main():
    if not valid(LINE):
        print("entry line fails the gate", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))
    return 0


def self_test():
    """Checks the gate's rejection cases and the boundary cases, then
    writes the entry and verifies the read-back byte for byte."""
    cases = [
        ("", False),
        ("   ", False),
        ("x" * 201, False),
        ("two\nlines", False),
        ("carriage\rreturn", False),
        (" leading", False),
        ("trailing ", False),
        ("tab\tinside", False),
        ("zero\u200bwidth", False),
        ("\ufeffonly", False),
        ("a", True),
        ("x" * 200, True),
        (LINE, True),
    ]
    failures = 0
    for text, expected in cases:
        got = valid(text)
        if got != expected:
            print("FAIL valid(%r) = %s, expected %s" % (text, got, expected))
            failures += 1
    rc = main()
    if rc != 0:
        print("FAIL main() returned %d" % rc)
        failures += 1
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print("self-test: all %d checks passed" % (len(cases) + 1))
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    sys.exit(main())
