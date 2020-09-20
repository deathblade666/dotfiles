#!/bin/bash
exec hsetroot -full ~/wallpapers/arch-wallpaper.png &
exec picom &
# Statusbar loop
while true; do
   xsetroot -name "$( date +"%F %R" )"
   sleep 1m    # Update time every minute
done &
