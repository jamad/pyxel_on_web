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
pyxel.colors[1]=0xff4040
pyxel.colors[2]=0x70c6a9
pyxel.colors[3]=0x4040ff

class App:
    def __init__(self):
        pyxel.init(screen_w, screen_h,display_scale=3)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.time_now=t = datetime.datetime.now()

        # center pos
        self.c = c = clock_r+1

        def get_x(multi, a):
            return c + int( clock_r * 0.3 * multi * cos (radians(a- 90)))
        def get_y(multi, a):
            return c + int( clock_r * 0.3 * multi * sin (radians(a- 90)))

        # second hand 
        sec_angle = (t.second + t.microsecond / 1000000) * 6 
        self.sec_x = get_x(3,sec_angle)
        self.sec_y = get_y(3,sec_angle)

        # minute hand 
        min_angle = (t.minute + t.second / 60) * 6 
        self.min_x = get_x(2,min_angle) 
        self.min_y = get_y(2,min_angle)
        
        # hour hand 
        hour_angle = (t.hour % 12 + t.minute / 60) * 30 
        self.hour_x = get_x(1,hour_angle)
        self.hour_y = get_y(1,hour_angle) 

    def draw(self):
        pyxel.cls(bg_color)

        c=self.c
        pyxel.circb(c, c, clock_r, fg_color)# clock outline
        pyxel.line(c, c, self.sec_x, self.sec_y, color_blue)
        pyxel.line(c, c, self.min_x, self.min_y, color_green)
        pyxel.line(c, c, self.hour_x, self.hour_y,  color_red)

        pyxel.text(20,6,f'{self.time_now.hour:02}:{self.time_now.minute:02}',7 )
        pyxel.text(26,48,f'{self.time_now.second:02}',7 )

App()
