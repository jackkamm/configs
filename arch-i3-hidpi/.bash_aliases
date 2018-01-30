#!/bin/bash

alias spotify="spotify --force-device-scale-factor=2"
alias openvpn="sudo openvpn --writepid /var/run/openvpn.pid --config"
alias feh="feh --keep-zoom-vp"
alias open="mimeopen"
alias warband="wine '/home/jack/.wine/drive_c/Program Files (x86)/Mount Blade Warband/mb_warband.exe'"

# replace Gnome/Gtk apps with KDE/Qt apps
# for better integration with i3+hidpi
alias gimp="krita"
alias nautilus="dolphin"

emacs () {
    /usr/bin/emacsclient -c $* || /usr/bin/emacs $*
}