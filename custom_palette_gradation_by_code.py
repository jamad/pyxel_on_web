import pyxel



class App:
    def __init__(self):
        pyxel.init(255, 81, title="Pyxel Custom Color Palette",display_scale=1 , fps=60)
        #pyxel.load('custom_palette_gradation.pyxres')

        #old_colors = pyxel.colors.to_list()
        pyxel.colors.from_list([0x555511]*11); pyxel.colors[15] = 0x112233
        print(pyxel.colors[15])
        print(hex(pyxel.colors[15]))

        s='''\
        000000
        081008
        102010
        183018
        204020
        285028
        306030
        387028
        408040
        489048
        50a050
        58b058
        60c060
        68d068
        70e070
        78f078'''.split()

        # for i,x in enumerate(s):
        #     v=eval('0x'+x)
        #     print(v)
        #     pyxel.colors[i]=v
        
        self.offset=0


        pyxel.run(self.update, self.draw)

    def update(self):
        
        for i,x in enumerate(range(0,0xffffff,528392)):
            pyxel.colors[i]=x + self.offset

        delta=0xffffff//32
        self.offset += delta
        self.offset %= 0xffffff


    def draw(self):
        pyxel.cls(0)
        for col in range(16):
            x,y = 2 + (col % 4) * 64, 4 + (col // 4) * 20
            
            rgb = pyxel.colors[col]
            
            hex = f"#{rgb:06X}"
            
            dec = f"{rgb >> 16},{(rgb >> 8) & 0xFF},{rgb & 0xFF}"
            
            #print('debug',col,rgb, hex, dec,len(pyxel.colors))

            pyxel.rect(x, y, 13, 13, col%16)
            pyxel.text(x + 16, y + 1, hex, 7)
            pyxel.text(x + 16, y + 8, dec, 7)
            pyxel.text(x + 5 - (col // 10) * 2, y + 4, f"{col}", 7 if col < 6 else 0)
            if col == 0:
                pyxel.rectb(x, y, 13, 13, 13)

App()
