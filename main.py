import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame  # noqa
from mascon import Master_Controller
import keymouse

def select_devices(dev_num=-1):
    pygame.init()
    if(dev_num == -1):
        device_num = pygame.joystick.get_count()
        if(device_num <= 0):
            raise ValueError("No device detected.")
        print("検出したJoystickの数:", device_num)
        controllers = [0]*device_num
        for i in range(device_num):
            controllers[i] = pygame.joystick.Joystick(i)
            device_name = controllers[i].get_name()
            print("デバイス%d: %s" % (i+1, device_name))
        selected_device_num = int(input("選択するデバイス番号: "))-1
        if(selected_device_num > device_num+1):
            raise ValueError(
                "The device No.%d is undefineed.".format(selected_device_num+1))
    else:
        selected_device_num = dev_num-1
    selected_device = pygame.joystick.Joystick(selected_device_num)
    selected_device.init()
    return selected_device


def convert_position(MasCon, inted_pos):  # マスコン位置に対応する位置(日本語)を返します、デバッグ用
    return MasCon.notch_table[inted_pos]

def get_button_status(device): # pygame.joystickオブジェクトを引数にとり、全てのbuttonの状態を配列で返します。
    pygame.event.pump()
    button_num=device.get_numbuttons()
    button_status=[device.get_button(i) for i in range(button_num)]
    return button_status


notch_table = ["EB", "B8", "B7", "B6", "B5", "B4",
               "B3", "B2", "B1", "N", "P1", "P2", "P3", "P4", "P5"]
notch_table_axes = [-1.0000000000, -0.9607849121, -0.8509826660, -0.7490234375, -0.6392211914, -0.5294189453, -0.4274597168, -
                    0.3176574707, -0.2078552246, 0.0039062500, 0.2470397949, 0.4352722168, 0.6156616211, 0.8038940430, 0.9999694824]
# 後で別の段数とか、個体差に対応できるように、ここで値を設定します。
ButtonNum_PushKey={0:'enter', 1:'b', 2:'backspace', 3:'e', 4:'t', 7:'k', 11:'up', 12:'down', 13:'x', 14:'space', 15:'w'}
# buttonIDと押すキーとの対応表

mascon = Master_Controller()
powercount = 5
bkcount = 8
frames=0

try:
    target_device=select_devices()
    mascon.set_data(target_device, notch_table,
                    notch_table_axes, powercount, bkcount)
    newtral_pos = mascon.step_count-powercount-1
    prev_pos = mascon.get_position()
    now_pos = prev_pos

    prev_button_status=get_button_status(target_device)
    now_button_status=prev_button_status

    print("Running...")
    while(True):
        now_pos = mascon.get_position()
        now_button_status=get_button_status(target_device)
        keymouse.mouse_scroller(prev_pos, now_pos, newtral_pos)
        keymouse.key_press(prev_button_status,now_button_status,ButtonNum_PushKey)
        prev_pos = now_pos
        prev_button_status=now_button_status
        frames=0
    
except Exception as err:
    print(err)
    time.sleep(3)
