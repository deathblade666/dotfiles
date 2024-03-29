
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

####################################
# Imports
###################################

import os
import re
import socket
import subprocess
from libqtile.command import lazy
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
myTerm = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "Right", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "Right", lazy.layout.shuffle_down()),
    Key([mod, "control"], "Left", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.group["Term"].toscreen(toggle=False), lazy.spawn("alacritty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "c", lazy.window.kill()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawn("dmenu_run -fn 'monospace:size=12' -nb #032541 -nf #ffffff ")),

    ################################################################
    # Custom Keybindings
    ################################################################
    Key([mod, "shift"], "e", lazy.group["Term"].toscreen(toggle=False), lazy.spawn("st" + ' -e ranger')),
    Key([mod, "shift"], "s", lazy.group["Games"].toscreen(toggle=False),lazy.spawn("steam")),
    Key([mod, "shift"], "p", lazy.spawn("./.config/scripts/qtile/screenshot.sh")),
    Key([mod, "shift"], "f", lazy.group["General"].toscreen(toggle=False),lazy.spawn("librewolf")),
    Key([mod, "shift"], "a", lazy.group["Developement"].toscreen(toggle=False), lazy.spawn("android-studio")),
    Key([mod, "shift"], "d", lazy.group["Music"].toscreen(toggle=False), lazy.spawn("deadbeef")),
]


##### GROUPS #####
group_names = [("General", {'layout': 'Tile'}),
            ("Term", {'layout': 'Tile'}),
	    ("Developement", {'layout': 'Tile'}),
	    ("Music", {'layout': 'Tile'}),
            ("Games", {'layout': 'Tile'}),
	    ("VM", {'layout': 'Tile'}),
	    ("Other", {'layout': 'Tile'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

#######################################
# Spawn Applications in specific Groups
#######################################

groups = [
	Group("General", matches=[Match(wm_class=["Vivaldi-stable"])]),	
	Group("Term", matches=[Match(title=['~'])]),
	Group("Developement", matches=[Match(wm_class=["jetbrains-studio"])]),
	Group("Music", matches=[Match(wm_class=["Deadbeef"])]),
	Group("Games", matches=[Match(wm_class=["Steam"]), Match(wm_class=["Lutris"])]),
	Group("VM", matches=[Match(wm_class=["Virt-manager"])]),
	Group("Other", matches=[Match(wm_class=["Barrier"])]),
]

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 1,
                "margin": 6,
                "border_focus": "#e78aba",
                "border_normal": "#032541",
                }

layouts = [
   # layout.Max(),
   # layout.Stack(),
   # Try more layouts by unleashing below layouts.
   # layout.Bsp(),
   # layout.MonadTall(),
   # layout.MonadWide(),
   # layout.RatioTile(),
    layout.Tile(ratio=.50, **layout_theme),
   # layout.TreeTab(),
   # layout.VerticalTile(),
   # layout.Zoomy(),
]

##### COLORS #####
# Sections are listed from left to right. A section is from the begining of one arrow in the bar to the begining of the next.
colors = [["#032541", "#032541"], # panel background
          ["#0c6583", "#0c6583"], # fifth section
          ["#5a3b5d", "#5a3b5d"], # fourth section
          ["#86618d", "#86618d"], # third section
          ["#903350", "#903350"], # second section
          ["#e784ba", "#e78aba"], # first section
          ["#ffffff", "#ffffff"]] # Text Color (White) 

##### PROMPT #####
#prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 0,
    background=colors[0]
)
#extension_defaults = widget_defaults.copy()

##### WIDGETS #####
def init_widgets_list():
    widgets_list = [
            
		widget.Sep(
                        linewidth=0,
                        padding=6,
                        background=colors[0],
                        foreground=colors[6],
                ),
                widget.GroupBox(),
		widget.WindowName(
			background=colors[0],
			foreground=colors[0],
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow.jpg",
		),
		widget.CPU(
			format='CPU {load_percent}%',
			background=colors[5],
			foreground=colors[6],
			padding=2,
		),
		widget.TextBox(
			text=" Thermal",
			background=colors[5],
			foreground=colors[6],
			padding=2,
		),
		widget.ThermalSensor(
			background=colors[5],
			foreground=colors[6],
			padding=2,
		),
                widget.TextBox(
                        text=" RAM",
                        background=colors[5],
                        foreground=colors[6],
                        padding=2,
               ),
               widget.Memory(
                        background=colors[5],
                        foreground=colors[6],
                        padding=5,
                ),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-blue.jpg",
		),
		widget.TextBox(
			text="Free Space",
			background=colors[4],
			foreground=colors[6],
			padding=2,
		),
		widget.DF(
			background=colors[4],
			foreground=colors[6],
			padding=5,
			update_interval=5,
			visible_on_warn=False,
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-red.jpg",
		),
		widget.TextBox(
			text="Network ",
			background=colors[3],
			foreground=colors[6],
		),
		widget.Net(
			format='{down} ↓↑ {up}',
			background=colors[3],
			foreground=colors[6],
			padding=4,
		),
		widget.TextBox(
			text = " ⟳",
			padding = 5,
			mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
			foreground = colors[6],
			background = colors[3],
			fontsize=14,
		),
		widget.CheckUpdates(
			update_interval = 180,
			display_format = "{updates} Updates",
			no_update_string= "0 Updates",
			distro = "Arch_checkupdates",
			background=colors[3],
			foreground=colors[6],
			padding=5,
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-purple.jpg",
		),
		widget.TextBox(
			text="Volume ",
			background=colors[2],
			foreground=colors[6],
			padding=2,
		),
		widget.Volume(
			background=colors[2],
			foreground=colors[6],
			padding=5,
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-purple2.jpg",
		),
                widget.Clock(
			format='%a %I:%M %p %m-%d-%Y',
			background=colors[1],
			foreground=colors[6],
		),
	    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [#Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button4", lazy.window.bring_to_front()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True
cursor_warp = False
floating_layout = layout.Floating(**layout_theme, float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='wine'),
    Match(title='vortex'),
])

##### STARTUP APPLICATIONS #####
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/scripts/qtile/startup.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
