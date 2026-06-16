#!/usr/bin/env py

import argparse
import os
import shutil
from pathlib import Path
import tomllib


def copy_file(src: Path | str, trg: Path | str, reverse: bool = False):
    src, trg = Path(src), Path(trg)
    os_suffix = "win" if os.name == "nt" else "linux"
    os_spec_src = Path(f"{src.with_suffix('')}-{os_suffix}{src.suffix}")
    if os_spec_src.is_file():
        src = os_spec_src  # we have specialized version

    if reverse:
        src, trg = trg, src

    assert src.is_file(), f"source file not found: {src}"
    shutil.copy(src, trg)
    print(f"{src} -> {trg}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--reverse",
        action="store_true",
        help="copy files from configured targets back into this settings repo",
    )
    args = parser.parse_args()

    with open("config.toml", "rb") as f:
        conf = tomllib.load(f)

    if "vscodium" in conf:
        vscodium_path = Path(conf["vscodium"])
        copy_file(
            "./vscodium/keybindings.json",
            vscodium_path / "User" / "keybindings.json",
            reverse=args.reverse,
        )
        copy_file(
            "./vscodium/settings.json",
            vscodium_path / "User" / "settings.json",
            reverse=args.reverse,
        )

    if "micro" in conf:
        micro_path = Path(conf["micro"])
        copy_file("./micro/bindings.json", micro_path / "bindings.json", reverse=args.reverse)
        copy_file("./micro/settings.json", micro_path / "settings.json", reverse=args.reverse)

    if "geany" in conf:
        geany_path = Path(conf["geany"])
        copy_file("./geany/geany.conf", geany_path / "geany.conf", reverse=args.reverse)
        copy_file(
            "./geany/keybindings.conf",
            geany_path / "keybindings.conf",
            reverse=args.reverse,
        )

    if "doublecmd" in conf:
        doublecmd_path = Path(conf["doublecmd"])
        copy_file(
            "./doublecmd/shortcuts.scf",
            doublecmd_path / "shortcuts.scf",
            reverse=args.reverse,
        )

    if "cursor" in conf:
        cursor_path = Path(conf["cursor"])
        copy_file(
            "./cursor/keybindings.json",
            cursor_path / "User" / "keybindings.json",
            reverse=args.reverse,
        )
        copy_file(
            "./cursor/settings.json",
            cursor_path / "User" / "settings.json",
            reverse=args.reverse,
        )

    print("settings sync complete!")


if __name__ == "__main__":
    main()
