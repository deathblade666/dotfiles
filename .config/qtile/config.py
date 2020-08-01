# Copyright (c) 2010 Aldo Cortesi
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
from libqtile.window import Window
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401


mod = "mod4"

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
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("st")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawn("rofi -modi run#ssh -show run")),

    ################################################################
    # Custom Keybindings
    ################################################################
    Key([mod], "b", lazy.spawn("qutebrowser")),
    Key([mod], "c", lazy.spawn("chromium")),
    Key([mod], "e", lazy.spawn("st" + ' -e ranger')),
    Key([mod], "s", lazy.spawn("steam")),
]


##### GROUPS #####
group_names = [("General", {'layout': 'tile'}),
               ("Term", {'layout': 'tile'}),
               ("Files", {'layout': 'tile'}),
               ("Games", {'layout': 'tile'}),
	       ("Media", {'layout': 'tile'}),
	       ("VM", {'layout': 'tile'}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group	

#######################################
# Spawn Applications in specific Groups
#######################################

groups = [
	Group("General", matches=[Match(wm_class=["qutebrowser", "Chromium"])]),	
	Group("Term", init=["True"], matches=[Match(wm_class=["st-256color"])]),
	Group("Files", matches=[Match(wm_class=["Pcmanfm"])]),
	Group("Games", matches=[Match(wm_class=["Steam"])]),	
	Group("Games", matches=[Match(wm_class=["Steam"])]),
	Group("Media", matches=[Match(wm_class=["mpv"]), Match(wm_class=["Gimp"])]),
	Group("VM", matches=[Match(wm_class=["Virt-manager"])]),
]

##### DEFAULT THEME SETTINGS FOR LAYOUTS #####
layout_theme = {"border_width": 1,
                "margin": 0,
                "border_focus": "#626584",
                "border_normal": "#303030",
                }

layouts = [
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
     layout.Tile(
	border_width = 1,
	border_focus = "#626584",
	border_normal = "#303030",
    ),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##### COLORS #####
colors = [["#303030", "#303030"], # panel background
          ["#887386", "#887386"], # Clock Background
          ["#ffffff", "#ffffff"], # text color (white)
          ["#626584", "#626584"], # background for system monitor widgets
          ["#704F56", "#704F56"], # background for network  widgets
          ["#263554", "#263554"], # background for control and update widgets
          ["#e1acff", "#e1acff"]] # 

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 0,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()


##### WIDGETS #####

screens = [
    Screen(
        top=bar.Bar(
            [
		widget.Sep(
                        linewidth=0,
                        padding=6,
                        background=colors[0],
                        foreground=colors[2],
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
			background=colors[4],
			foreground=colors[2],
			padding=2,
		),
		widget.TextBox(
			text=" Thermal",
			background=colors[4],
			foreground=colors[2],
			padding=2,
		),
		widget.ThermalSensor(
			background=colors[4],
			foreground=colors[2],
			padding=2,
		),
                widget.TextBox(
                        text=" RAM",
                        background=colors[4],
                        foreground=colors[2],
                        padding=2,
               ),
               widget.Memory(
                        background=colors[4],
                        foreground=colors[2],
                        padding=5,
                ),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-blue.jpg",
		),
		widget.TextBox(
			text="Network ",
			background=colors[5],
			foreground=colors[2],
		),
		widget.Net(
			format='{down} ↓↑ {up}',
			background=colors[5],
			foreground=colors[2],
			padding=4,
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-purple.jpg",
		),
		widget.TextBox(
			text="🔊 ",
			background=colors[3],
			foreground=colors[2],
		),
		widget.Volume(
			background=colors[3],
			foreground=colors[2],
			padding=2
		),
		widget.TextBox(
			text=" ↻ ",
			background=colors[3],
			foreground=colors[2],
		),
		widget.CheckUpdates(
			display_format='{updates}',
			background=colors[3],
			foreground=colors[2],
			update_interval=1800,
			padding=4,
		),
		widget.Image(
			filename="~/.config/qtile/pictures/arrow-purple2.jpg",
		),
                widget.Clock(
			format='%a %I:%M %p %m-%d-%Y',
			background=colors[1],
			foreground=colors[2],
		),
            ],
            24,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

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
