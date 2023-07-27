import pyxel
from math import radians, cos, sin
import datetime

clock_r = 28
screen_w = clock_r*2+3
screen_h = clock_r*2+3
bg_color=0
fg_color=7

# color palette change by code
color_red=1
color_green=2
color_blue=3
pyxel.colors[1]=0xff0000
pyxel.colors[2]=0x70c6a9
pyxel.colors[3]=0x0000ff


class App:
    def __init__(self):
        pyxel.init(screen_w, screen_h,display_scale=2)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.time_now = datetime.datetime.now()

    def draw(self):
        pyxel.cls(bg_color)

        # center coord
        cx = cy = clock_r+1

        # clock outline
        pyxel.circb(cx, cy, clock_r, fg_color)

        # second hand to disp
        sec_angle = (self.time_now.second + self.time_now.microsecond / 1000000) * 6 - 90
        sec_x = cx + int(clock_r * 0.9 * cos(radians(sec_angle)))
        sec_y = cy + int(clock_r * 0.9 * sin(radians(sec_angle)))
        pyxel.line(cx, cy, sec_x, sec_y, color_blue)

        # minute hand to disp
        min_angle = (self.time_now.minute + self.time_now.second / 60) * 6 - 90
        min_x = cx + int(clock_r * 0.6 * cos(radians(min_angle)))
        min_y = cy + int(clock_r * 0.6 * sin(radians(min_angle)))
        pyxel.line(cx, cy, min_x, min_y, color_green)

        # hour hand to disp
        hour_angle = (self.time_now.hour % 12 + self.time_now.minute / 60) * 30 - 90
        hour_hand_len=clock_r * 0.3
        hour_dx = int(hour_hand_len * cos(radians(hour_angle)))
        hour_dy = int(hour_hand_len * sin(radians(hour_angle)))
        pyxel.line(cx, cy, cx+hour_dx, cy+hour_dy,  color_red)

App()
