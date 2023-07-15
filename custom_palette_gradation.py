import pyxel



class App:
    def __init__(self):
        pyxel.init(255, 81, title="Pyxel Custom Color Palette",display_scale=1)
        pyxel.load('custom_palette_gradation.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for col in range(16):
            x,y = 2 + (col % 4) * 64, 4 + (col // 4) * 20
            
            rgb = pyxel.colors[col]
            
            hex = f"#{rgb:06X}"
            
            dec = f"{rgb >> 16},{(rgb >> 8) & 0xFF},{rgb & 0xFF}"
            
            #print('debug',col,rgb, hex, dec,len(pyxel.colors))

            pyxel.rect(x, y, 13, 13, col%16)
            pyxel.text(x + 16, y + 1, hex, 7)
            pyxel.text(x + 16, y + 8, dec, 7)
            pyxel.text(x + 5 - (col // 10) * 2, y + 4, f"{col}", 7 if col < 6 else 0)
            if col == 0:
                pyxel.rectb(x, y, 13, 13, 13)

App()
