import pyxel
import datetime

class App:
    def __init__(self):
        pyxel.init(33, 7, title='Time Display',display_scale=4)
        self.current_time = datetime.datetime.now().strftime('%H:%M:%S')

        pyxel.run(self.update, self.draw)

    def update(self):
        self.current_time = datetime.datetime.now().strftime('%H:%M:%S')

    def draw(self):
        pyxel.cls(0)
        pyxel.text(1, 1, self.current_time, 7)

App()
