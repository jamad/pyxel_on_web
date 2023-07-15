import pyxel
import math
import datetime

class App:
    def __init__(self):
        pyxel.init(200, 200, title='Analog Clock')
        pyxel.clock(self.update, 60)
        self.current_time = datetime.datetime.now()

        pyxel.run(self.draw)

    def update(self):
        self.current_time = datetime.datetime.now()

    def draw(self):
        pyxel.cls(7)

        # 時計の中心座標
        center_x = pyxel.width // 2
        center_y = pyxel.height // 2

        # 時計の半径
        radius = 80

        # 時計の外枠を描画
        pyxel.circb(center_x, center_y, radius, 0)

        # 時針を描画
        hour_angle = (self.current_time.hour % 12 + self.current_time.minute / 60) * 30 - 90
        hour_x = center_x + int(radius * 0.4 * math.cos(math.radians(hour_angle)))
        hour_y = center_y + int(radius * 0.4 * math.sin(math.radians(hour_angle)))
        pyxel.line(center_x, center_y, hour_x, hour_y, 0)

        # 分針を描画
        minute_angle = (self.current_time.minute + self.current_time.second / 60) * 6 - 90
        minute_x = center_x + int(radius * 0.6 * math.cos(math.radians(minute_angle)))
        minute_y = center_y + int(radius * 0.6 * math.sin(math.radians(minute_angle)))
        pyxel.line(center_x, center_y, minute_x, minute_y, 0)

        # 秒針を描画
        second_angle = (self.current_time.second + self.current_time.microsecond / 1000000) * 6 - 90
        second_x = center_x + int(radius * 0.8 * math.cos(math.radians(second_angle)))
        second_y = center_y + int(radius * 0.8 * math.sin(math.radians(second_angle)))
        pyxel.line(center_x, center_y, second_x, second_y, 8)

App()
