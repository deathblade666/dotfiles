#!/bin/zsh
exec hsetroot -full ~/Pictures/wallpapers/Wolf.jpg &
exec filen.appimage &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
picom --no-fading-openclose &
xset s off &
export BROWSER="/usr/bin/oqutebrowser"
if [ -n "$DESKTOP_SESSION" ];then
        eval $(gnome-keyring-daemon --start)
	export SSH_AUTH_SOCK
fi


# Statusbar loop

sep="|"

bar()  (\
    
    # cpu temps
    CPU=$(sensors | sed -rn 's/.*Package id 0:\s+.([^ ]+).*/\1/p')
    echo "CPU Temp: $CPU"

    echo "$sep"

    memUsage=$(free -m | awk '/Mem/{print $3}')
    echo "RAM: $memUsage MB"

    echo "$sep"

    swap=$(free -m | awk '/Swap/{print $3}')
    echo "Swap $swap MB"

    echo "$sep"

    # gpu temps
    GPU=$(nvidia-smi --format=nounits,csv,noheader --query-gpu=temperature.gpu)
    echo "GPU Temp: $GPU °C"

    echo "$sep"

    # date
    echo "$( date +"%D  %I:%M " )"

)



while :; do
    xsetroot -name "$(bar | tr '\n' ' ')"
    sleep 1s
done &
