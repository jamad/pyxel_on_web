# -*- coding: utf-8 -*-
import pyxel
import sys
print(sys.executable) # check which pything is running

# constant variables
screen_width=160
screen_height=120
character_width=11
character_height=8
my_disp_scale=2
my_fps=60
my_asset="assets/practice_invader.pyxres"
character_posY=30

class App:
    
    def __init__(self): 
        pyxel.init(screen_width, screen_height, title="invader", display_scale=my_disp_scale, fps=my_fps)
        pyxel.load(my_asset)
        
        self.image_posY_to_draw= 0
        pyxel.run(self.update, self.draw) 

    def update(self):            
        self.image_posY_to_draw= (pyxel.frame_count % 20 < 10 ) * 8

    def draw(self): 
        pyxel.cls(0)# clear screen
        speedX=5
        posX = (pyxel.frame_count //speedX) % pyxel.width
        pyxel.blt(posX , character_posY, 0, 0, self.image_posY_to_draw, 11, 8, 0)
        
        if screen_width - character_width < posX: # double drawing if not full drawing
            pyxel.blt(posX -screen_width , character_posY, 0, 0, self.image_posY_to_draw, 11, 8, 0)

        pyxel.text(10, 10, "FRAME COUNT: "+str(pyxel.frame_count), 10)

App()
