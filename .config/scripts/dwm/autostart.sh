#!/bin/zsh
exec hsetroot -full ~/Pictures/wallpapers/Wolf.jpg &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# picom --experimental-backend &
barriers -f --no-tray --debug INFO --name ArchLinux --enable-crypto -c /tmp/Barrier.oivgih --address :24800 &

# Statusbar loop


sep="|"

bar()  (\
    
    # cpu temps
    CPU=$(sensors | sed -rn 's/.*Package id 0:\s+.([^ ]+).*/\1/p')
    echo "CPU Temp: $CPU"

    echo "$sep"

    # gpu temps
    GPU=$(nvidia-smi --format=nounits,csv,noheader --query-gpu=temperature.gpu)
    echo "GPU Temp: $GPU"

    echo "$sep"

    # date
    echo "$( date +"%D  %I:%M " )"

)



while :; do
    xsetroot -name "$(bar | tr '\n' ' ')"
    sleep 1s
done &
