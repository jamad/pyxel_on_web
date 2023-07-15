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

SCR_W=96
SCR_H=54
W=H=16

class App:
    def __init__(self):
        pyxel.init(SCR_W, SCR_H, title="Image by code", display_scale=2)
        self.color = 1
        self.img_id = 0
        pyxel.image(self.img_id).set(0, 0, art.split())

        pyxel.run(self.update, self.draw)

    def update(self):
        self.color += pyxel.btnp(pyxel.KEY_SPACE)
        if 15 <= self.color: self.color = 1

    def draw(self):
        pyxel.cls(0)
        
        pyxel.pal(7, self.color)
        pyxel.blt((SCR_W - W) // 2, (SCR_H - H) // 2, self.img_id, 0, 0, W, H, 0)
        pyxel.pal()

        pyxel.text(0, 0, 'col change by SPACE: ' + str(self.color), 7)

App()