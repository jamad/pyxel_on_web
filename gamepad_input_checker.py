import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 256, title='gamepad input', display_scale=2)

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

App()
