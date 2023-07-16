
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

class App:
    def __init__(self):
        pyxel.init(width, height, title="mandelbrot", display_scale=my_disp_scale, fps=my_fps)
        
        #custom palette 
        pyxel.load('custom_palette_gradation.pyxres')

        self.data = {}
        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.data:
            for r in range(height):
                for c in range(width):
                    a = (c - center_x) / scaling
                    b = (r - center_y) / scaling
                    iteration = self.calculate_iteration(complex(a, b))
                    self.data[(r, c)] = iteration

    def draw(self):
        pyxel.cls(0) 

        for r in range(height):
            for c in range(width):
                iteration = self.data[(r, c)]
                color = self.get_color(iteration)
                pyxel.pset(c, r, color)

    def calculate_iteration(self, c, z=0, iteration_level=16):
        for i in range(iteration_level):
            z = z * z + c
            if abs(z) > 2:
                return i
        return iteration_level

    def get_color(self, iteration):
        color = iteration * 7 // 16  # color mapping
        return color

App()
