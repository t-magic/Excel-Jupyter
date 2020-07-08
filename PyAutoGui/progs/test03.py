

# [PyAutoGUIでマウス操作などのGUI操作する方法 - 白猫学生のブログ]
# (https://whitecat-student.hatenablog.com/entry/2016/06/27/010812)

import pyautogui

# マウスカーソルの現在の座標の取得方法
print(pyautogui.position())  # 現在のマウスのxとy座標を返す

# ディスプレイの解像度の取得方法
print(pyautogui.size())  #ディスプレイの解像度を返す

# マウスカーソルが画面内に存在するか確認する方法
x = 100
y = 100
print(pyautogui.onScreen(x, y))  # もし画面内にあればTrueを返す)

# GUI操作を行うごとにプログラムを一時停止する設定方法
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True # Falseで無効

# クリック操作
x = 100
y = 100
time = 1
pyautogui.moveTo(x, y, time)  # マウスカーソルを (x,y)の座標までtime秒で移動する．もしtime=0であればすぐに移動する．
xOffset = 100
yOffset = 200
pyautogui.moveRel(xOffset, yOffset, time)  #現在のマウスカーソルの座標から(xOffset,yOffset)だけtime秒で移動する．
print('-' * 50)

pyautogui.click(50, 100, 2, 0.5, 'left')
print('-' * 50)

pyautogui.rightClick(x,y)  #右クリック
pyautogui.middleClick(x,y) #真ん中クリック
pyautogui.doubleClick(x,y) #ダブルクリック
pyautogui.tripleClick(x,y) #トリプルクリック
print('-' * 50)

pyautogui.dragTo(x, y, time)  #現在のマウスカーソルの座標から(x,y)の座標までtime秒でドラッグする．
pyautogui.dragRel(xOffset, yOffset, time)  # 現在のマウスカーソルの座標から(xOffset，yOffset)だけtime秒でドラッグし移動する

pyautogui.mouseDown(x, y, button='left')
pyautogui.mouseUp(x, y, button='left')

amount_to_scroll = 1
#pyautogui.scroll(amount_to_scroll, x, y)

interval = 1
pyautogui.typewrite('Hello world!\n', interval)  # intervalは文字間の入力待機時間です．
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval) #配列にも対応しています．

print(pyautogui.KEYBOARD_KEYS)
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
# '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
# '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
# 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
# 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps',
# 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert',
# 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end',
# 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15',
# 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5',
# 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home',
# 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert',
# 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9',
# 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack',
# 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock',
# 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop',
# 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft',
# 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

key_name = 'X'
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)