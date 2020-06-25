#!/bin/zsh

CPU=$(sensors | sed -rn 's/.*Package id 0:\s+.([^ ]+).*/\1/p')

# Full and short texts
echo "$CPU"

exit 0
