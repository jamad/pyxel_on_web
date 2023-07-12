import pyxel

class App:
    def __init__(self): 
        pyxel.init(160, 120, title="move rect by arrow keys")
        self.x = self.y = 0
        pyxel.run(self.update, self.draw) 

    def update(self): # calc data
        self.x += (pyxel.btn(pyxel.KEY_RIGHT))    - (pyxel.btn(pyxel.KEY_LEFT))
        self.y += (pyxel.btn(pyxel.KEY_DOWN))     - (pyxel.btn(pyxel.KEY_UP))
      
    def draw(self): # draw data
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 5, 5, 6) 
      
App()
