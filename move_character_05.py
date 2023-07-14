# -*- coding: utf-8 -*-
import pyxel
import sys
print(sys.executable) # check which pything is running

# constant variables (rare to change)
screen_width=160
screen_height=120
my_disp_scale=2
my_fps=60

# for this app
from time import gmtime, strftime

class App:
    
    def __init__(self): 
        pyxel.init(screen_width, screen_height, title="time display", display_scale=my_disp_scale, fps=my_fps)
        self.my_time="-" # initial declaration for time to display
        pyxel.run(self.update, self.draw) 

    def update(self):            
        self.my_time=strftime("%Y-%m-%d %H:%M:%S", gmtime()) # update time to display
        

    def draw(self): 
        pyxel.cls(0)# clear screen
        pyxel.text(10, 10, f"TIME: {self.my_time}", 10) # display text

App()
