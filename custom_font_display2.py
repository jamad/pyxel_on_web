# reference - https://ytyaru.hatenablog.com/entry/2022/04/13/000000

from PIL import Image, ImageFont, ImageDraw
import pyxel
import string
import os
import numpy as np


fontfile_path = os.path.join(os.path.dirname(__file__), 'x8y12pxTheStrongGamer.ttf') # relative path based on this .py file

ascii_chars = string.punctuation + string.digits + string.ascii_letters
hiragana = "".join(chr(c) for c in range(ord('ぁ'), ord('ゔ') + 1)) + "ー"
katakana = "".join(chr(c) for c in range(ord('ァ'), ord('ヶ') + 1)) + "ー"
string_to_disp = f'font: {fontfile_path} {"-"*32}{ascii_chars + hiragana + katakana + "、。「」"}'

screen_w=256
screen_h=128+8

class App:
    def __init__(self):
        pyxel.init(screen_w, screen_h, title="Custom Font Display", display_scale=1)
        
        # font data 
        px_w, px_h = (8, 12)
        img = Image.new('1', size=(256, 256))
        x, y = 0, 0
        for c in string_to_disp:
            if x + px_w > 256:
                #print(x)
                x = 0
                y += px_h
            ImageDraw.Draw(img).text((x, y), c, font=ImageFont.truetype(fontfile_path, size=px_h), fill=1)
            x += px_w
        self.font_data = np.array(img.getdata()).reshape(256, 256)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        img=0
        color=7# white color
        img_bank = pyxel.image(img)
        for y in range(256):
            for x in range(256):
                if self.font_data[y][x] != 0:
                    pyxel.pset(x, y, color) 

App()