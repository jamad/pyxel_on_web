import pyxel

class App:
    def __init__(self):
        pyxel.init(64, 32, title="Hello Pyxel",display_scale=2)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(8, 16, "Hello, Pyxel!", pyxel.frame_count % 16)
        
App()
