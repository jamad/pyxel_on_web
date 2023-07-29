import pyxel

my_img='''\
0000000000000000
00a0000000000a00
00a0000000000a00
0000000000000000
0333300000033330
0000000000000000
0333000000003330
3000300000030003
3070309009030703
3000300000030003
0333000000003330
0000000000800000
0000200000000000
0002220080008000
0000200000000000
0000000000800000
'''.split() 

my_img=[''.join(str(int('0'<c)) for c in line) for line in my_img ]
        
#print(my_img)

class App:
    def __init__(self):
        pyxel.init(256, 256, title='gamepad input', display_scale=2)
        self.img_id=0
        pyxel.image(self.img_id).set(0, 0, my_img) # assigning string list to image(0)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        gamepadnum='GAMEPAD1_'
        direction='LEFTX LEFTY RIGHTX RIGHTY TRIGGERLEFT TRIGGERRIGHT'.split()

        for i,x in enumerate(direction):
            data_to_check=gamepadnum + 'AXIS_' + x
            pyxel.text(10,10+10*i, f'{data_to_check} : {pyxel.btnv(eval("pyxel."+ data_to_check))}', 7)

        button='A B X Y BACK GUIDE START LEFTSTICK RIGHTSTICK LEFTSHOULDER RIGHTSHOULDER DPAD_UP DPAD_DOWN DPAD_LEFT DPAD_RIGHT'.split()
        for i,x in enumerate(button):
            data_to_check=gamepadnum + 'BUTTON_' + x
            value=pyxel.btn(eval("pyxel."+ data_to_check))
            pyxel.text(10,80+10*i, f'{data_to_check} : {value}', value and 7 or 2)

            
        pyxel.blt(200, 10, self.img_id, 0, 0, 16, 16, 0)
        pyxel.text(200,40, f'wip',  1)

App()
