# reference - https://ytyaru.hatenablog.com/entry/2022/04/13/000000

from PIL import Image, ImageFont, ImageDraw
import pyxel
import string
import numpy as np

import os

hiragana = "".join(map(chr,range(ord('ぁ'), ord('ゔ')+1))) 
katakana = "".join(map(chr,range(ord('ァ'), ord('ヶ')+1))) 

screen_w=256
screen_h=256

def font_gen(filename, dx, dy): #dx, dy : font dimension
    fontfile_path = os.path.join(os.path.dirname(__file__), filename) # relative path based on this .py file
    font_to_use=ImageFont.truetype(fontfile_path, size=dy)
    string_to_disp = f'{filename}{" "*(256//12)}{string.punctuation}{string.digits}{string.ascii_letters}{hiragana}ー{katakana}ー、。「」{" "*7}適当な漢字を追加でテスト'
    font_image = Image.new('1', size=(256, 256)) # fontimage generation : 256x256
    for i,c in enumerate(string_to_disp):
        y,x=divmod(dx*i, 256)
        ImageDraw.Draw(font_image).text((x, y*dy), c, font=font_to_use, fill=1)
    return np.array(font_image.getdata()).reshape(256, 256)

class App:
    def __init__(self):
        pyxel.init(screen_w, screen_h, title="Custom Font Display", display_scale=1)
        
        self.font_flag=0

        # font data generation : # both fonts from http://www17.plala.or.jp/xxxxxxx/00ff/ 
        self.font_data1 = font_gen('x8y12pxTheStrongGamer.ttf',8, 12) 
        self.font_data2 = font_gen('x12y16pxMaruMonica.ttf',12, 16)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT):self.font_flag = 0
        if pyxel.btn(pyxel.KEY_RIGHT):self.font_flag = 1
        
    def draw(self):
        pyxel.cls(0)

        color=7 # white color

        for y in range(screen_h):
            for x in range(screen_w):
                
                if self.font_flag:
                    pyxel.pset(x, y, self.font_data1[y][x] and color) 
                else:
                    pyxel.pset(x, y, self.font_data2[y][x] and color) 

App()