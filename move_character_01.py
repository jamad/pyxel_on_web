# -*- coding: utf-8 -*-

# assets/cat_16x16.png
# jump_game.pyxres

import pyxel

class App:
    def __init__(self): # 初期化
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw) # アプリケーションの実行

    def update(self): # フレームの更新処理

        # 右キーを押している間はxが増える
        self.x = self.x + 1 if(pyxel.btn(pyxel.KEY_RIGHT)) else 1
            
        #self.x = (self.x + 1) % pyxel.width

    def draw(self): # 描画処理
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)



App()
