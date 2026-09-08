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

from libqtile import qtile, hook
from libqtile.config import Click, Drag, Group, Key
from libqtile.lazy import lazy
from settings import mod
import build_keys
import build_screens
import build_layouts
import os
import subprocess
# import mypy
# import psutil

# Autostart
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home], shell=True)

@hook.subscribe.client_new
def make_everything_floating(window):
    def _bring_to_front():
        group = window.group
        if group and group.layout.__class__.__name__.lower() == "floating":
            window.floating = True
            window.bring_to_front()
            window.focus(warp=True)

    qtile.call_later(0.1, _bring_to_front)

keys = build_keys.keys

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),

            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key(
            #     [mod, "shift"], 
            #     i.name, 
            #     lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)
            # ),
        ]
    )

layouts = build_layouts.layouts

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def charge_controller(battery):
    # Custom charge controller logic
    if battery.percent < 80:
        return True
    return False

screens = build_screens.screens

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
