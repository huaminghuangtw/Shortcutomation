#!/usr/bin/env python3

"""Build the shortcut backup zips from the `All Shortcuts/` folder.

Only `.shortcut` files (the importable shortcuts) are included; all other
artifacts (.html/.json/.plist/.png) are excluded to keep the archives small.

Outputs:
  <outdir>/All_Shortcuts_with_Folders.zip    - .shortcut files, folder structure
                                               preserved
  <outdir>/All_Shortcuts_without_Folders.zip - .shortcut files flattened to the
                                               zip root

Usage:
  python3 build_release_zips.py [src_dir] [out_dir]
"""

import os
import sys
import zipfile

DEFAULT_SRC = "All Shortcuts"


def _iter_shortcuts(src: str):
    for root, _dirs, files in os.walk(src):
        for fn in files:
            if fn.endswith(".shortcut"):
                yield os.path.join(root, fn)


def build_with_folders(src: str, outdir: str) -> str:
    out = os.path.join(outdir, "All_Shortcuts_with_Folders.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for full in _iter_shortcuts(src):
            arc = os.path.relpath(full, src)
            z.write(full, arc)
    return out


def build_without_folders(src: str, outdir: str) -> str:
    out = os.path.join(outdir, "All_Shortcuts_without_Folders.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for full in _iter_shortcuts(src):
            z.write(full, os.path.basename(full))
    return out


def main() -> None:
    args = sys.argv[1:]
    src = args[0] if len(args) > 0 else DEFAULT_SRC
    outdir = args[1] if len(args) > 1 else "."
    os.makedirs(outdir, exist_ok=True)
    a = build_with_folders(src, outdir)
    b = build_without_folders(src, outdir)
    print(f"created {a} ({os.path.getsize(a) / 1e6:.1f} MB)")
    print(f"created {b} ({os.path.getsize(b) / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
