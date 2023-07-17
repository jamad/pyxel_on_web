import pyxel, random

width=160
height=120

rect_size=32
rect_color=3
noise_range=4

class App:
    def __init__(self):
        pyxel.init(width, height,display_scale=1)
        self.x= 0
        self.y= 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x= (width // 2)  + random.randint(-noise_range, noise_range)
        self.y= (height// 2)  + random.randint(-noise_range, noise_range)
    
    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, rect_size, rect_color)
        pyxel.circb(self.x, self.y, rect_size, 7)

App()