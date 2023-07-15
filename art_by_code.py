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
        pyxel.init(96, 54, title="Image by code", display_scale=2)
        
        self.x = (96 - 16) // 2
        self.y = (54 - 16) // 2
        self.img = 0
        self.w = self.h = 16
        self.color = 1
        pyxel.image(0).set(0, 0, art.split())

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.color += 1
            if 15 <= self.color: self.color = 1

    def draw(self):
        pyxel.cls(0)
        
        pyxel.pal(7, self.color)
        pyxel.blt(self.x, self.y, self.img, 0, 0, self.w, self.h, 0)
        pyxel.pal()

        pyxel.text(0, 0, 'col change by SPACE: ' + str(self.color), 7)

App()