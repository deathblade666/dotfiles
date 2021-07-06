#!/bin/bash
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
hsetroot -full $HOME/Pictures/wallpapers/scenery.jpg &
barriers --no-tray --debug INFO --name ArchLinux --enable-crypto -c /home/deathmasia/.config/barrier/Barrier --address :24800 &
picom &


