"""Tiny exact-string patch helper used during development: patch(path, [(old, new), ...]).
Fails loudly if an `old` string is missing; always writes LF line endings."""
import pathlib


def patch(path, reps):
    p = pathlib.Path(path)
    s = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    for old, new in reps:
        if old not in s:
            raise SystemExit(f"{path}: not found: {old[:70]!r}")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8", newline="\n")
