#!/bin/bash

export $(dbus-launch)
export XDG_CURRENT_DESKTOP=qtile
export XDG_SESSION_TYPE=x11
export XDG_SESSION_DESKTOP=qtile
export QT_QPA_PLATFORMTHEME=gtk2

start() {
	if ! pgrep -f "$1";
	then
		"$@"&
	fi
}
# start feh --bg-fill "/home/eric/Pictures/Wallpaper/360671.png" &
start /usr/libexec/at-spi-bus-launcher --launch-immediately &
start /usr/libexec/at-spi2-registryd &
start xfsettingsd &
start nm-applet & 
start blueman-applet &
start /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
start start-pulseaudio-x11 &
start light-locker & 
start /usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd &
start xiiccd &
start xfce4-power-manager &
start $HOME/.local/share/ABDownloadManager/bin/ABDownloadManager --background & 
start xdg-desktop-portal &
start xdg-desktop-portal-gtk &

python3 $HOME/.config/qtile/batteryLimit.py &
