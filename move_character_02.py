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

            
        # マウスカーソルの座標を取得
        self.mx = pyxel.mouse_x
        self.my = pyxel.mouse_y


    def draw(self): # 描画処理
        pyxel.cls(0)
        # 新しく四角形を作成
        # 左上の座標をマウスカーソルの座標と一致させる
        pyxel.rect(self.mx, self.my, 5, 5, 6)



App()
