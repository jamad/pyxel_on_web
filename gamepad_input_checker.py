import pyxel

####  下記のデータをアルファベットで表現すれば、26個以内でキーの状態に応じて、対応する部分のドットの色付けをできそうな気がする

my_img='''\
0000000000000000
00c0000000000d00
00c0000000000d00
0000000000000000
0mmmm000000nnnn0
0000000000000000
0333000000003330
3000300000030003
30k030i00j030l03
3000300000030003
0333000000003330
0000000000h00000
0000o00000000000
000q2r00g000f000
0000p00000000000
0000000000e00000
'''.split() 

KEYPOS=[]    
for x in 'abcdefghizjklmnopqrstuv':
    data=[''.join(f'{int(c==x)}' for c in line) for line in my_img ]
    KEYPOS.append(data)
    print(data)
#print(my_img)

my_img=[''.join(str(int('0'<c)) for c in line) for line in my_img ]

image_base=0
image_triggered=1


class App:
    def __init__(self):
        pyxel.init(256, 256, title='gamepad input', display_scale=2)

        pyxel.image(image_base).set(0, 0, my_img) # assigning string list to image(0)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        
        my_img_trigger=[['0']*16 for _ in range(16)]

        gamepadnum='GAMEPAD1_'
        direction='LEFTX LEFTY RIGHTX RIGHTY TRIGGERLEFT TRIGGERRIGHT'.split() # a a b b c d 

        for i,x in enumerate(direction):
            data_to_check=gamepadnum + 'AXIS_' + x
            pyxel.text(10,10+10*i, f'{data_to_check} : {pyxel.btnv(eval("pyxel."+ data_to_check))}', 7)

        button='A B X Y BACK GUIDE START LEFTSTICK RIGHTSTICK LEFTSHOULDER RIGHTSHOULDER DPAD_UP DPAD_DOWN DPAD_LEFT DPAD_RIGHT'.split() # e f g h i z j k l m n o p q r
        for i,x in enumerate(button):
            #print(i,x)
            data_to_check=gamepadnum + 'BUTTON_' + x
            value=pyxel.btn(eval("pyxel."+ data_to_check))
            pyxel.text(10,80+10*i, f'{data_to_check} : {value}', value and 7 or 2)

            if value:
                for r in range(16):
                    for c in range(16):
                        if KEYPOS[i+4][r][c]=='1':
                            if my_img_trigger[r][c]=='0':
                                my_img_trigger[r][c]='7'

        pyxel.blt(200, 10, image_base, 0, 0, 16, 16, 0) # gamepad base image

        pyxel.image(image_triggered).set(0, 0, [''.join(R) for R in my_img_trigger]) # assigning data for highlight to image(1)
        pyxel.blt(200, 10, image_triggered, 0 ,0, 16, 16, 0)

        pyxel.text(200,40, f'wip',  1)

App()
