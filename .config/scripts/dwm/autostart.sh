#!/bin/bash
exec hsetroot -full ~/Pictures/wallpapers/Wolf.jpg &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# Statusbar loop
while true; do
   xsetroot -name "$( date +"%D  %I:%M " )"
   sleep 1m    # Update time every minute
done &
