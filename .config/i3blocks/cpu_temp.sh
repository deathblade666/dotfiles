#!/bin/zsh

CPU=$(sensors | sed -rn 's/.*CPU:\s+.([^ ]+).*/\1/p')

# Full and short texts
echo "$CPU"

exit 0
