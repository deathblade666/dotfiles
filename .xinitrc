# Here qtile is kept as default
session=${1:-qtile}

case $session in
    i3|i3wm           ) exec i3;;
    qtile             ) exec qtile;;
    xfce|xfce4        ) exec startxfce4;;
    # No known session, try to run it as command
    *                 ) exec $1;;
esac
