
# -*- coding: utf-8 -*-
import pyxel

# constant variables
width = 160
height = 120
my_disp_scale=1
my_fps=60

# for this app
center_x=width//2
center_y=height//2
scaling=max(width,height)//3


def mandelbrot(c, z=0, iteration_level=30): # true if dot stay 
    for i in range(iteration_level):
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
            for r in range(height):
                for c in range(width):
                    a = (c - center_x) /scaling
                    b = (r - center_y) /scaling
                    self.data[(r,c)]=mandelbrot(complex(a, b))

    def draw(self): 
        pyxel.cls(0)# clear screen
    
        for r in range(height):
            for c in range(width):
                dotcolor=7*self.data[(r,c)] # black or white color
                pyxel.pset(c, r, dotcolor)

App()