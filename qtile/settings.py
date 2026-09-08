from libqtile import qtile
import subprocess

mod = "mod4"
terminal = "alacritty"

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

def powermenu(qtile):
    subprocess.run(["bash ~/.config/rofi/powermenu/type-1/powermenu.sh"], shell=True)
def rofi(qtile):
    # subprocess.run(["bash ~/.config/rofi/launchers/type-2/launcher.sh"], shell=True)
    subprocess.run(["rofi -show drun"], shell=True)
