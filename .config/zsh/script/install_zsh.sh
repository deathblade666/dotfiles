#!/bin/bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" <<< exit
git clone https://github.com/powerline/fonts.git ~/fonts
git clone git://github.com/sigurdga/gnome-terminal-colors-solarized.git ~/.solarized
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh-autosuggestions
fc-cache -f -v
cd ~/fonts
./install.sh
cd ~/.solarized
./install.sh


