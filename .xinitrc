numlockx &
export _JAVA_AWT_WM_NONREPARENTING=1
# Here qtile is kept as default
session=${1:-qtile}

case $session in
    i3|i3wm           ) exec i3;;
    qtile             ) exec qtile;;
    xfce|xfce4        ) exec startxfce4;;
    dwm               ) exec dwm;;
    plasma|kde	      ) exec startplasma-x11;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac
