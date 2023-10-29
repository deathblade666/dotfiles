#!/bin/bash
exec maim -f png -u -o -s | tee ~/Pictures/screenshots/$(date +%Y-%b-%d--%H-%M-%S).png | xclip -selection clipboard -t image/png

#path="~/Pictures/screenshots/$(date +%Y-%b-%d--%H-%M-%S).png" && maim -s "$path" && xclip -selection clipboard -t image/png "$path"
