from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Columns(
        border_normal='#000',
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_focus=["#90b262"],
        border_width=1,
        margin=0,
    ),
    layout.Max(),
    layout.Floating(
        border_width=2,
        border_focus='#90b262',
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            # use 'xprop | grep WM_CLASS'
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(wm_class="com-abdownloadmanager-desktop-AppKt"),
            Match(wm_class="com-abdownloadmanager-desktop-AppKt"),
            Match(wm_class="heidisql"),
            Match(wm_class="Qt6EmbedWindow"),
            Match(title="Completion"),
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(title="InputOutput"),
            Match(title="Completion"),
            Match(title="Add Download"),
        ]
    ),
]

