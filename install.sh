#!/bin/zsh
pacman -S --noconfirm ebtables fakeroot sudo dnsmasq archiso libvirt virt-manager git curl wget alsa-utils wpa_supplicant polkit-gnome zsh go base-devel htop nfs-utils vi vim hsetroot neofetch rofi i3-gaps xorg xorg-xinit qemu ovmf nvidia chromium qutebrowser steam ranger pcmanfm mpv <<< Y
systemctl enable libvirtd
mkdir /home/deathmasia/NAS
echo '192.168.86.232:/NAS/NAS01 /home/deathmasia/NAS nfs defaults,_netdev 0 0' >> /etc/fstab

