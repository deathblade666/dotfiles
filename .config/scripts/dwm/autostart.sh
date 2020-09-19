#!/bin/bash
xrandr -s 1920x1080 &
exec hsetroot -full ~/Wallpapers/wallpaper.jpg &
exe picom &
# Statusbar loop
while true; do
   xsetroot -name "$( date +"%F %R" )"
   sleep 1m    # Update time every minute
done &
