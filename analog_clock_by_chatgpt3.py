import pyxel
from math import radians, cos, sin
import datetime

clock_r = 28
screen_width = clock_r*2+3
screen_height = clock_r*2+3
background_color=0
foreground_color=7
color_red=8
color_green=11
color_blue=12

class App:
    def __init__(self):
        pyxel.init(screen_width, screen_height,display_scale=2)
        pyxel.load('analog_clock_by_chatgpt3.pyxres')
        
        print(len(pyxel.colors))
        
        for i,x in enumerate( pyxel.colors):
            print(i,x,hex(x))

        print(pyxel.colors)
        

        self.time_now = datetime.datetime.now()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.time_now = datetime.datetime.now()

    def draw(self):
        pyxel.cls(background_color)

        # 時計の中心座標
        cx = cy = clock_r+1

        # 時計の外枠を描画
        pyxel.circb(cx, cy, clock_r, foreground_color)



        # 秒針を描画
        second_angle = (self.time_now.second + self.time_now.microsecond / 1000000) * 6 - 90
        second_x = cx + int(clock_r * 0.9 * cos(radians(second_angle)))
        second_y = cy + int(clock_r * 0.9 * sin(radians(second_angle)))
        pyxel.line(cx, cy, second_x, second_y, color_blue)

        # 分針を描画
        minute_angle = (self.time_now.minute + self.time_now.second / 60) * 6 - 90
        minute_x = cx + int(clock_r * 0.6 * cos(radians(minute_angle)))
        minute_y = cy + int(clock_r * 0.6 * sin(radians(minute_angle)))
        pyxel.line(cx, cy, minute_x, minute_y, color_green)

        # 時針を描画
        hour_angle = (self.time_now.hour % 12 + self.time_now.minute / 60) * 30 - 90
        hour_hand_len=clock_r * 0.3
        hour_dx = int(hour_hand_len * cos(radians(hour_angle)))
        hour_dy = int(hour_hand_len * sin(radians(hour_angle)))
        pyxel.line(cx, cy, cx+hour_dx, cy+hour_dy,  color_red)

App()
