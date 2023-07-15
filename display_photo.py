import pyxel
pyxel.init(256,256,display_scale=2)
pyxel.cls(0)

#custom palette 
pyxel.load('custom_palette_gradation.pyxres')

# loading image based on the palette
pyxel.image(0).load(0, 0, "my_photo.png")
pyxel.blt(0,0, 0, 0,0, 256,256)

pyxel.text(10,210,"full color -> custom palette",15)

pyxel.show()

