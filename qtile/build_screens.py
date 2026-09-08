from libqtile import bar, widget
from libqtile.config import Screen

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TaskList(
                    highlight_method='block',
                    icon_size=25,
                    background='#0A0E14',
                    margin_y=0,
                    padding_y=5,
                ),
            ],
            25,
        ),
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(highlight_method='line'),
                widget.Prompt(),
                widget.Spacer(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("&lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Sep(),
                widget.CapsNumLockIndicator(fmt="{}"),
                widget.Sep(),
                widget.CPU(
                    format='CPU {freq_current}GHz {load_percent}%',
                    update_interval=1.0,
                    foreground="#ffffff",
                    background="#3a3d7d",
                    ),
                widget.Memory(
                    format='Mem{MemUsed: .0f}{mm}/{MemPercent: .0f}%',
                    update_interval=1.0,
                    foreground='#ffffff',
                    background='#7d7c40',
                    ),
                widget.Sep(),
                widget.Battery(
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                    charge_char="⚡",
                    discharge_char="🔋",
                    full_char="🔌",
                    empty_char="❗",
                    not_charging_char="❌🔌",
                    unknown_char="❓",
                    update_interval=1,
                    battery=0,  # Battery index, usually 0
                    notify_below=20,
                    low_background="#ff5757",
                    foreground="#ffffff",
                    background="#347e38",
                    #charge_controller=lambda: charge_controller(psutil.sensors_battery())
                    ),
                widget.Sep(),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.TextBox("Vol:"),
                widget.Volume(
                    volume_app='pavucontrol',
                    update_interval=0.1,
                ),
                widget.Sep(),
                widget.Systray(),
                widget.Sep(),
                widget.Clock(format="%a,%d-%m-%Y|%I:%M %p"), #%Y-%m-%d %a %I:%M %p
                widget.Sep(),
                widget.QuickExit(
                    default_text="[ X ]"
                ),
            ],
            24,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=["90b262", "000000", "90b262", "000000"],  # Borders are magenta
            background='#0A0E14',
        ),
        x11_drag_polling_rate = 60,
    ),
]

