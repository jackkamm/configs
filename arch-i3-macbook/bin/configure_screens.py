#!/usr/bin/env python
import subprocess as sub
import argparse

laptop_x = 2560
laptop_y = 1600

def run(cmd, *args, **kwargs):
    print(*cmd)
    sub.run(cmd, *args, **kwargs)

def configure_screens(scale):
    lines = sub.run(
        ["xrandr"], stdout=sub.PIPE,
        universal_newlines=True).stdout.split("\n")

    lines = iter(lines)
    for l in lines:
        l = l.split()
        if len(l) >= 2:
            if l[0] != "eDP1" and l[1] == "connected":
                output = l[0]
                preferred_res = next(lines).split()[0]
                x, y = map(int, preferred_res.split("x"))
                cmd = [
                    "xrandr", "--output", output, "--auto",
                    "--mode", f"{x}x{y}",
                    "--panning", f"{scale*x}x{scale*y}+{laptop_x}+0",
                    "--scale", f"{scale}x{scale}",
                    "--right-of", "eDP1"]
                run(cmd)
            elif l[1] == "disconnected":
                cmd = ["xrandr", "--output", l[0], "--off"]
                run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scale", type=int, default=2)
    args = parser.parse_args()

    run(["xrandr", "--output", "eDP1", "--primary",
         "--mode", "2560x1600", "--pos", "0x0",
         "--rotate", "normal"])

    configure_screens(args.scale)
