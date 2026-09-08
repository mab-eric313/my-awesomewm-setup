from libqtile.lazy import lazy
from libqtile.config import Key
from settings import mod, terminal, powermenu, rofi

keys = [
    Key([mod], "h", lazy.group.prev_window(), lazy.window.bring_to_front(), desc="Move focus to previous window"),
    Key([mod], "l", lazy.group.next_window(), lazy.window.bring_to_front(), desc="Move focus to next window"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Control volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 5%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 5%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),

    # Applications
    Key([mod, "shift"], "d", lazy.function(rofi), desc="Launch Rofi drun"),
    Key([mod, "shift"], "Return", lazy.spawn("thunar"), desc="Launch thunar File Manager"),

    # Powermenu
    Key([mod, "shift"], "q", lazy.function(powermenu), desc="Launch Rofi powermenu"),
]

