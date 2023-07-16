
# -*- coding: utf-8 -*-
import pyxel

# constant variables

s = 1  # cell size
width = 256
height = 256
ws = max(width,height) # windows size
my_disp_scale=1
my_fps=60

# for this app

def mandelbrot(c,z=0, iteration_level=30):
    for _ in range(iteration_level):
        z = z * z + c
        if abs(z) > 2:
            return False
    return True

class App:
    
    def __init__(self): 
        pyxel.init(width, height, title="mandelbrot", display_scale=my_disp_scale, fps=my_fps)
        self.data={}
        pyxel.run(self.update, self.draw) 

    def update(self):   
        if not self.data:
            for r in range(ws):
                for c in range(ws):
                    a = (c - ws // 2) / (ws // 4)
                    b = (r - ws // 2) / (ws // 4)
                    self.data[(r,c)]=mandelbrot(complex(a, b))

    def draw(self): 
        pyxel.cls(0)# clear screen
    
        for r in range(height):
            for c in range(width):
                dotcolor=7*self.data[(r,c)] # black or white color
                pyxel.pset(c, r, dotcolor)

App()