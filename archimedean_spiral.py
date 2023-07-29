import pyxel
from math import pi

coords = []
limit = 1e4
between_distace = 0.05

class App:
    def __init__(self):
        pyxel.init(256, 256, title='Archimedean spiral', display_scale=2,fps=60)
        pyxel.camera(-pyxel.width/2, -pyxel.height/2) # offset
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        count=pyxel.frame_count

        if limit < count: return
        dist, angle = between_distace * count, pi* count
        coords.append( (dist*pyxel.cos(angle), dist*pyxel.sin(angle)) )

    def draw(self):
        pyxel.cls(0)

        for i,coord in enumerate(coords[::-1]):
            pyxel.pset(coord[0], coord[1], i%16)

        pyxel.text(10,120, f'dot count :{pyxel.frame_count}', 8)


App()
