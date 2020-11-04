#!/bin/bash

batter=cat /sys/class/power_supply/BAT0/capacity

exec hsetroot -full ~/wallpapers/arch-wallpaper.png &
# Statusbar loo
exec ~/.config/scripts/dwm/bar.sh &
