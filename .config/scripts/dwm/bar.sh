#!/bin/bash

delim="|"

bar() (\
# starting separator
	echo "$delim"	

# Battery
	echo "BAT:"
	bat= cat /sys/class/power_supply/BAT0/capacity	
	echo "$bat%"

# Separator
	echo "$delim"

# Date
	date '+%a, %b %D %I:%M%p'
	)

# While loop to update every 1 minute
while :; do
	xsetroot -name "$(bar | tr '\n' ' ')"
	sleep 1m
done
