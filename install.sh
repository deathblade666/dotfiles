#!/bin/zsh

## More work is needed for this

#install applications
pacman -S --noconfirm ebtables fakeroot sudo dnsmasq archiso libvirt virt-manager git curl wget alsa-utils wpa_supplicant polkit-gnome zsh go base-devel htop nfs-utils vi vim hsetroot neofetch rofi i3-gaps xorg xorg-xinit qemu ovmf nvidia chromium qutebrowser steam ranger pcmanfm mpv <<< Y

# Enabled services
systemctl enable libvirtd

# Creat mount points for nfs share and add to /etc/fstab
mkdir /home/deathmasia/NAS
echo '192.168.86.232:/NAS/NAS01 /home/deathmasia/NAS nfs defaults,_netdev 0 0' >> /etc/fstab

# cloning and installing oh-my-zsh and powerline fonts 
git clone https://github.com/deathblade666/dotfiles.git /home/deathmasia/
cd ~/.config/zsh/script
chmod +x install_zsh.sh
./install_zsh.sh

mv ~/.oh-my-zsh/oh-my-zsh.sh ~/.oh-my-zsh/oh-my-zsh.sh.bak
cp ~/.conifg/zsh/oh-my-zsh/oh-my-zsh.sh ~/.oh-my-zsh/oh-my-zsh.sh
mv ~/.zshrc ~/.zshrc.bak
cp ~/.config/zsh/.zshrc ~/.zshrc

# install yay and st terminal
git clone https://aur.archlinux.org/yay.git ~/yay
cd ~/yay
makepkg -si
yay -S st <<< N
