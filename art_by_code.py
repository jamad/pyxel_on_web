import pyxel

my_img='''\
.....######.....
...##......##...
..#..........#..
.#............#.
.#........#...#.
#....#...#.....#
#....#....#....#
#..............#
#......##......#
#......##......#
#...#......#...#
.#...#....#.#.#.
.#....####....#.
..#..........#..
...##......##...
.....######.....
'''

my_img=[''.join('07'[c=='#'] for c in line) for line in my_img.split() ]
#print(my_img)

SCR_W=96
SCR_H=54
W=H=16

class App:
    def __init__(self):
        pyxel.init(SCR_W, SCR_H, title="Image by code", display_scale=2)
        self.color = 1
        self.img_id = 0
        pyxel.image(self.img_id).set(0, 0, my_img)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.color += pyxel.btnp(pyxel.KEY_SPACE)
        if 15 <= self.color: self.color = 1

    def draw(self):
        pyxel.cls(0)
        
        pyxel.pal() # reset palette
        pyxel.text(0, 0, 'col change by SPACE: ' + str(self.color), 7)
        
        pyxel.pal(7, self.color) # override color 7 
        pyxel.blt((SCR_W - W) // 2, (SCR_H - H) // 2, self.img_id, 0, 0, W, H, 0)

App()