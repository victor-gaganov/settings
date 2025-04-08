#!/usr/bin/bash

SETTINGS=/home/user/settings

VSCODIUM=/home/user/.config/VSCodium
cp "$SETTINGS/vscodium/keybindings.json" "$VSCODIUM/User/keybindings.json" || exit 1
cp "$SETTINGS/vscodium/settings.json" "$VSCODIUM/User/settings.json" || exit 1

MICRO=/home/user/.config/micro
cp "$SETTINGS/micro/bindings.json" "$MICRO/bindings.json" || exit 1
cp "$SETTINGS/micro/settings.json" "$MICRO/settings.json" || exit 1

GEANY=/home/user/.config/geany
cp "$SETTINGS/geany/geany.conf" "$GEANY/geany.conf" || exit 1
cp "$SETTINGS/geany/keybindings.conf" "$GEANY/keybindings.conf" || exit 1

DOUBLECMD=/home/user/.config/doublecmd
cp "$SETTINGS/doublecmd/doublecmd.xml" "$DOUBLECMD/doublecmd.xml" || exit 1
cp "$SETTINGS/doublecmd/shortcuts.scf" "$DOUBLECMD/shortcuts.scf" || exit 1

CURSOR=/home/user/.config/Cursor
cp "$SETTINGS/cursor/keybindings.json" "$CURSOR/User/keybindings.json" || exit 1
cp "$SETTINGS/cursor/settings.json" "$CURSOR/User/settings.json" || exit 1

echo "Settings applied successfully!"
