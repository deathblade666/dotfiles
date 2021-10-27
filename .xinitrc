dbus-update-activation-environment --systemd DISPLAY &
numlockx &
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh) &
export SSH_AUTH_SOCK &
xset s off &
export _JAVA_AWT_WM_NONREPARENTING=1
exec /usr/local/bin/dwm
