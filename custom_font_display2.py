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


def draw_font(img, font, col=7):
    img_bank = pyxel.image(img)
    for y in range(256):
        for x in range(256):
            if font.data[y][x] != 0:
                pyxel.pset(x, y, col)


def update():
    pass


def draw():
    pyxel.cls(0)
    draw_font(0, font)


fontfile = 'x8y12pxTheStrongGamer.ttf'
letter_size = (8, 12)
ascii_chars = string.punctuation + string.digits + string.ascii_letters
hiragana = "".join(chr(c) for c in range(ord('ぁ'), ord('ゔ') + 1)) + "ー"
katakana = "".join(chr(c) for c in range(ord('ァ'), ord('ヶ') + 1)) + "ー"
alphabet = ascii_chars + hiragana + katakana + "、。「」"

font = Font(fontfile, letter_size, alphabet)

pyxel.init(256, 256, title="Custom Font Display")
pyxel.run(update, draw)
