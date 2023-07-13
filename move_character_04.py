# -*- coding: utf-8 -*-
import sys
print(sys.executable)
#exit()

import pyxel
pyxel.init(128, 128, title="invader", display_scale=2, fps=6)
pyxel.load("assets/practice_invader.pyxres")
def update():
	"""NONE"""
def draw():
	pyxel.cls(1)
	pyxel.blt(pyxel.frame_count % pyxel.width, 60, 0, 0, 8*(pyxel.frame_count % 2), 11, 8, 0)
pyxel.run(update, draw)
