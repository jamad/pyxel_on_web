import pyxel
pyxel.init(128,128,display_scale=1)
pyxel.cls(0)

#custom palette 
pyxel.load('custom_palette_gradation.pyxres')

# loading image based on the palette
pyxel.image(0).load(0, 0, "my_photo.png")
pyxel.blt(0,0, 0, 64,64, 128,128)

pyxel.show()

