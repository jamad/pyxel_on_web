# reference - https://ytyaru.hatenablog.com/entry/2022/04/13/000000
# fixed the error by chatting with chatgpt3.5

from PIL import Image, ImageFont, ImageDraw
import pyxel
import string

class Font:
    def __init__(self, file, size, alphabet):
        import numpy as np
        self.file = file
        self.size = size
        self.alphabet = alphabet

        px_w, px_h = size
        font = ImageFont.truetype(file, size=px_h)
        img = Image.new('1', size=(256, 256))
        draw = ImageDraw.Draw(img)
        coords = {}
        x, y = 0, 0
        for c in alphabet:
            if x + px_w > 256:
                x = 0
                y += px_h
            draw.text((x, y), c, font=font, fill=1)
            coords[c] = (x, y)
            x += px_w
        self.coords = coords
        self.img = img
        self.data = np.array(img.getdata()).reshape(256, 256)

fontfile = 'x8y12pxTheStrongGamer.ttf'
char_size = (8, 12)
ascii_chars = string.punctuation + string.digits + string.ascii_letters
hiragana = "".join(chr(c) for c in range(ord('ぁ'), ord('ゔ') + 1)) + "ー"
katakana = "".join(chr(c) for c in range(ord('ァ'), ord('ヶ') + 1)) + "ー"
alphabet = ascii_chars + hiragana + katakana + "、。「」"
font = Font(fontfile, char_size, alphabet)

class App:
    def __init__(self):
        pyxel.init(256, 256, title="Custom Font Display", display_scale=2)
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
                if font.data[y][x] != 0:
                    pyxel.pset(x, y, color) 

App()