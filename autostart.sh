#!/bin/bash

conky -dc $HOME/.config/awesome/system-overview
#feh --bg-fill ~/.config/awesome/default/5fa66423c18fcdf85af6c318d82bae08ad22.png &
/usr/libexec/at-spi-bus-launcher --launch-immediately &
/usr/libexec/at-spi2-registryd &
xfsettingsd &
nm-applet & 
blueman-applet &
/opt/freedownloadmanager/fdm --hidden &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
start-pulseaudio-x11 &
light-locker & 
mintreport-tray &
mintupdate-launcher &
/usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd &
xiiccd &
xfce4-power-manager &
volumeicon &
