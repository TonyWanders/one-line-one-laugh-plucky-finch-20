#!/usr/bin/env python3
"""One Line, One Laugh (plucky-finch-20 instance).

Writes one funny one-line laugh to the output target:
argv[1], else $OUTPUT_PATH, else /output/entry.txt.
Standard library only. Deterministic: same output every run.
"""

import os
import sys

LINE = (
    "My smartwatch congratulated me on 10,000 steps today, which is generous, "
    "since 9,000 of them were me pacing around overthinking a text I sent in 2019."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MIN_ENTRY_LENGTH = 1
MAX_ENTRY_LENGTH = 200


def validate_entry(text):
    """Enforce the competition's 1-200 character gate for the entry line."""
    length = len(text)
    if length < MIN_ENTRY_LENGTH or length > MAX_ENTRY_LENGTH:
        raise ValueError(
            "entry must be between %d and %d characters, got %d"
            % (MIN_ENTRY_LENGTH, MAX_ENTRY_LENGTH, length)
        )
    return text


def resolve_output_path(argv=None):
    """Pick the output target: argv[1], else $OUTPUT_PATH, else the default."""
    args = sys.argv if argv is None else argv
    if len(args) > 1 and args[1]:
        return args[1]
    env_path = os.environ.get("OUTPUT_PATH")
    if env_path:
        return env_path
    return DEFAULT_OUTPUT_PATH


def write_entry(path, text):
    """Validate the entry, then write it plus a trailing newline to path."""
    validated = validate_entry(text)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated + "\n")
    return path


def main():
    target = resolve_output_path()
    write_entry(target, LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
