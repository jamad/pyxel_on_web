import pyxel



class App:
    def __init__(self):
        pyxel.init(255, 255, title="Pyxel Custom Color Palette",display_scale=2,fps=240)
        pyxel.load('custom_palette_gradation.pyxres')
        pyxel.run(self.update, self.draw)

    def update(self):
        # マウスカーソルの座標を取得
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y

    def draw(self):
        pyxel.cls(0)

        # small grid
        for x in range(0,256,16):
            for y in range(0,256,16):
                pyxel.rect(x+self.mx%16, y+self.my%16, 1, 1, 3)

        # large grid
        for x in range(0,256,32):
            for y in range(0,256,32):
                pyxel.rect(x+self.mx%32 -1, y+self.my%32 -1, 3, 3, 5)
        
        # circle
        pyxel.circb(self.mx, self.my,7,12)
            

App()
