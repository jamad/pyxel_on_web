import pyxel

art='''\
0000077777700000
0007700000077000
0070000000000700
0700000000000070
0700000000000070
7000070000700007
7000070000700007
7000000000000007
7000000000000007
7000000000000007
7000700000070007
0700070000700070
0700007777000070
0070000000000700
0007700000077000
0000077777700000
'''
print(art.split())

class App:
    def __init__(self):
        pyxel.init(96, 54, title="Image API", display_scale=2)
        self.niko = Niko()
        pyxel.run(self.update, self.draw)

    def update(self):
        self.niko.update()

    def draw(self):
        pyxel.cls(0)
        self.niko.draw()
        pyxel.text(0, 0, 'Please SPACE key: ' + str(self.niko.color), 7)

class Niko:
    def __init__(self):
        self.__set_image0()
    
    def __set_image0(self):
        self.x = (96 / 2) - (16 / 2)
        self.y = (54 / 2) - (16 / 2)
        self.img = 0
        self.u = self.v = 0
        self.w = self.h = 16
        self.color = 7
        pyxel.image(0).set(0, 0, art.split())

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.__change_color()

    def draw(self):
        pyxel.pal(7, self.color)
        pyxel.blt(self.x, self.y, self.img, 0, 0, self.w, self.h, 0)
        pyxel.pal()

    def __change_color(self):
        self.color += 1
        if 15 <= self.color: self.color = 1

App()