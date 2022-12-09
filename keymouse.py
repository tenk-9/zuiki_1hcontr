import pyautogui
Mouse_scroll_delta = 125
EBscroll = 10000

def mouse_scroller(prev_pos, now_pos, newtral_pos):
    if (prev_pos == now_pos):
        pass
    else:
        if (now_pos == newtral_pos):  # N位置ならホイールクリック
            pyautogui.click(button='middle')
        elif (now_pos == 0):
            pyautogui.scroll(10000)  # EB位置なら上方向に思いっきり回転
        else:
            delta = prev_pos-now_pos
            pyautogui.scroll(delta*Mouse_scroll_delta)
            # ゲーム上ではマウスホイールでの操作として認識させます。
            # 検証したところ、1段あたりだいたい130"click"だと適切に動作します。値が小さいと、コントローラでB7に入れてもゲーム上でB6になるなどします。
            # 値は環境に依存するかもしれません。
            # delta<0で下スクロール、delta>0で上スクロールです。


def key_press(prev_btnstatus, now_btnstatus, ButtonNum_Key_Table):
    # 前回のボタン状態配列、現在のボタン状態配列、ボタンの番号と押すべきキーの対応辞書を引数にとります。
    for button_num, keyname in ButtonNum_Key_Table.items():
        if (prev_btnstatus[button_num] < now_btnstatus[button_num]):  # status 0->1: 押された
            pyautogui.keyDown(keyname)
        elif (prev_btnstatus[button_num] > now_btnstatus[button_num]):  # status 1->0: 離された
            pyautogui.keyUp(keyname)
        else:
            pass
