import pyxel
import numpy as np

screensize = 128
margin = 10
shape_orig_size = screensize - margin * 2
anim_speed=10

class HeartShapeApp:
    def __init__(self):
        pyxel.init(screensize, screensize, display_scale=2)

        self.t = np.linspace(0, 2 * np.pi, 1000)
        x = 16 * np.sin(self.t)**3
        y = 13 * np.cos(self.t) - 5 * np.cos(2 * self.t) - 2 * np.cos(3 * self.t) - np.cos(4 * self.t)
        self.x = (x - np.min(x)) / (np.max(x) - np.min(x)) * shape_orig_size
        self.y = (y - np.min(y)) / (np.max(y) - np.min(y)) * shape_orig_size
        self.cx, self.cy = np.mean(self.x), np.mean(self.y)
        
        self.heart_size = shape_orig_size
        self.is_animating= False

        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_animating:
            self.heart_size += anim_speed
            if shape_orig_size <= self.heart_size :
                self.heart_size = shape_orig_size
                self.is_animating= False
        elif ( pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_SPACE) ):
            self.is_animating = True
            self.heart_size=shape_orig_size * 0.5

    def draw(self):
        pyxel.cls(0)

        for i in range(len(self.x)):
            x_pos = int((screensize / 2) + (self.x[i] - self.cx) * self.heart_size / shape_orig_size)
            y_pos = margin + int((screensize / 2) + (self.y[i] - self.cy) * self.heart_size / shape_orig_size)
            pyxel.pset(x_pos, screensize - y_pos, 8)

HeartShapeApp()
