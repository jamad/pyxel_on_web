# reference - https://ytyaru.hatenablog.com/entry/2022/04/13/000000

from PIL import Image, ImageFont, ImageDraw
import pyxel
import string
import numpy as np

import os

filename='x8y12pxTheStrongGamer.ttf'
fontfile_path = os.path.join(os.path.dirname(__file__), filename) # relative path based on this .py file

hiragana = "".join(map(chr,range(ord('ぁ'), ord('ゔ')+1))) 
katakana = "".join(map(chr,range(ord('ァ'), ord('ヶ')+1))) 
string_to_disp = f'font: {filename} {"-"*32}{string.punctuation}{string.digits}{string.ascii_letters}{hiragana}ー{katakana}ー、。「」'

screen_w=256
screen_h=128+8
dx, dy = (8, 12) # font dimension
my_font=ImageFont.truetype(fontfile_path, size=dy)

class App:
    def __init__(self):
        pyxel.init(screen_w, screen_h, title="Custom Font Display", display_scale=1)
        
        # font data generation : self.font_data
        font_image = Image.new('1', size=(256, 256)) # fontimage generation : 256x256
        for i,c in enumerate(string_to_disp):
            y,x=divmod(dx*i, 256)
            ImageDraw.Draw(font_image).text((x, y*dy), c, font=my_font, fill=1)

        self.font_data = np.array(font_image.getdata()).reshape(256, 256)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        color=7 # white color

        for y in range(screen_h):
            for x in range(screen_w):
                pyxel.pset(x, y, self.font_data[y][x] and color) 

App()