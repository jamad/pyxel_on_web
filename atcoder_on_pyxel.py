
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
# input simulation practicePython\atcoder\at_coder_input_sample.py

import io
import sys

_INPUT = """\
2
1 2 3
aaa
"""

sys.stdin = io.StringIO(_INPUT)

a=int(input())
b=list(map(int, input().split()))
c=list(input())


class App:
    
    def __init__(self): 
        pyxel.init(screen_width, screen_height, title="time display", display_scale=my_disp_scale, fps=my_fps)
        pyxel.run(self.update, self.draw) 

    def update(self):            
        pass

    def draw(self): 
        pyxel.cls(0)# clear screen

        #print(a) #2
        #print(b) #[1, 2, 3]
        #print(c) #['a', 'a', 'a']
        pyxel.text(10, 0, f" {a}", 10) # display text
        pyxel.text(10, 10, f" {b}", 10) # display text
        pyxel.text(10, 20, f" {c}", 10) # display text
        

App()
