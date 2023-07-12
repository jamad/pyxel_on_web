# -*- coding: utf-8 -*-

import pyxel

class App:
    def __init__(self): # 初期化
        pyxel.init(160, 120)
        self.x = self.y = 0
        pyxel.run(self.update, self.draw) 

    def update(self): # calc data
        self.x += (pyxel.btn(pyxel.KEY_RIGHT))
        self.x -= (pyxel.btn(pyxel.KEY_LEFT))
        self.y += (pyxel.btn(pyxel.KEY_DOWN))
        self.y -= (pyxel.btn(pyxel.KEY_UP))
      
    def draw(self): # draw data
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 5, 5, 6) 
      
App()
