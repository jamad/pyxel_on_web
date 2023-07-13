# -*- coding: utf-8 -*-
import pyxel
pyxel.init(128, 128, caption="invader", scale=4, fps=5)
pyxel.load("invader_resource.pyxres")
def update():
	"""NONE"""
def draw():
	pyxel.cls(1)
	pyxel.blt(pyxel.frame_count % pyxel.width, 60, 0, 0, 8*(pyxel.frame_count % 2), 11, 8, 0)
pyxel.run(update, draw)
