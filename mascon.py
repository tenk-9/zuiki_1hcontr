from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame  # noqa


class Master_Controller:
    def __init__(self):  # pygame.joystickオブジェクト、ノッチ情報、ノッチ段数、各ノッチでのaxisの値、P段数、BK段数を持ちます。
        self.device = 0
        self.notch_table = []
        # 例えば["EB","B8","B7","B6","B5",…,"P2","P3","P4","P5"]、P5B8以外にも対応できるようにしました。
        self.step_count = 0
        self.notches_axesvalue = []
        # 例えば[-1.0000000000, -0.9607849121, -0.8509826660,…, 0.8038940430, 0.9999694824]、個体差があるかもしれないので最初に設定します。段数を変更したい場合は、この値を工夫します。
        # notch_table[]とnotches_axisvalue[]は当然同じ長さです。
        self.multiply_size = 100
        # 測定時に四捨五入されるなどして生じうる小さな誤差を許容するために、notches_axesvalue[]の値を整数に丸めます。その倍率。
        self.power_steps = 0
        self.normalbrake_steps = 0
    


    def set_data(self, device, notch_table, notches_axesvalue, power_steps, normalbrake_steps):
        self.device = device
        self.notch_table = list(notch_table)
        self.step_count = len(self.notch_table)
        self.notches_axesvalue = list(notches_axesvalue)
        self.power_steps = power_steps
        self.normalbrake_steps = normalbrake_steps
        for i in range(self.step_count):
            axis_val = self.notches_axesvalue[i]
            self.notches_axesvalue[i] = int(axis_val * self.multiply_size)
            # 整数に丸めこんで小さな誤差を許容します。先述。

    def get_position(self):  # マスコンの位置をintで返します
        pygame.event.pump()
        position_raw = self.device.get_axis(1)
        position_inted = int(position_raw*self.multiply_size)
        position_decided = False
        for i in range(len(self.notch_table)):
            if(position_inted == self.notches_axesvalue[i]):
                position_decided = True
                return i
        if(position_decided == False):
            raise ValueError(
                "Failed to decide a position of controller.")
    
