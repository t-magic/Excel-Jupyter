#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip
import pyautogui

import time
import os
import datetime

time.sleep(5)
def get_appli_region(topLeftCorner_png, bottomRightCorner_png, tracep = True):
    # 上の左隅の座標を求める。
    top_left_corner_box = pyautogui.locateOnScreen(topLeftCorner_png, grayscale=True, confidence=0.9)
    top_left_corner = top_left_corner_box[0:2]
    if tracep:
        print(f"top_left_corner = {top_left_corner}")

    # 下の右隅の座標を求める。
    bottom_right_corner_box = pyautogui.locateOnScreen(bottomRightCorner_png, grayscale = True, confidence = 0.9)
    print(f"bottom_right_corner_box = {bottom_right_corner_box}")
    # bottom_right_corner_box = Box(left=669, top=805, width=230, height=77)
    bottom_right_corner = [bottom_right_corner_box[0] + bottom_right_corner_box[2], \
                           bottom_right_corner_box[1] + bottom_right_corner_box[3]]

    if tracep:
        print(f"bottom_right_corner = {bottom_right_corner}")

    # アプリケーションのGUIの箱座標(左, 上, 右, 下)を返す。
    return [top_left_corner[0], top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1]]

def click_to_save_wav_file(wav_file_path):
    # アプリのGUIの左上隅と右下隅の画像を入力して、その二つで作るアプリの矩形を得る。
    appli_region = get_appli_region("../data/png/AITalk_TopLeftCorner.png", \
                                    "../data/png/AITalk_BottomRightCorner.png")
    print(f"appli_region = {appli_region}")
    # ファイルメニューは左上隅にしていいので、こうする。
    top_left_region = [max(appli_region[0] - 50, 0), max(appli_region[1] - 50, 0), \
                       min(appli_region[0] + 300, 1920), min(appli_region[1] + 100, 1080)]
    print(f"top_left_region = {top_left_region}")

    x, y = pyautogui.locateCenterOnScreen("../data/png/AITalk_File.png", region = top_left_region)
    print(x, y)
    # fileをクリックする。
    pyautogui.click(x, y)
    # 音声ファイルを保存を選ぶ
    pyautogui.typewrite('V')
    # WAV形式で保存を選ぶ
    pyautogui.hotkey('f7')
    time.sleep(1)
    # ファイル名をタイプする
    pyautogui.typewrite(wav_file_path)
    # enterする
    pyautogui.press('enter')
    # 保存している時間、待つ
    time.sleep(1)

click_to_save_wav_file(r'Z:\ScanKindle\PyTorch_clean_text_voice\test.wav')


'''この後は、
1. テキストを全部選んで消す。(Ctrl-A, Ctrl-X)

'''
"""
while True:
    time.sleep(5)
    print('.', end = "")
    try:
        # プレイボタンが戻ってきた。
        print(f"ret = {ret}")
        if pyautogui.locateOnScreen("../data/png/AITalk_Play.png", region=(930, 530, 1140, 680)) != None:
            break
    except:
        pass
print('finish')"""


"""# 上の左隅の座標を求める。
top_left_corner_box = pyautogui.locateOnScreen("../data/png/AITalk_TopLeftCorner.png", grayscale = True, confidence = 0.9)
top_left_corner = top_left_corner_box[0:2]
print(f"top_left_corner = {top_left_corner}")


# 下の右隅の座標を求める。
bottom_right_corner_box = pyautogui.locateOnScreen("../data/png/AITalk_BottomRightCorner.png", grayscale = True, confidence = 0.9)
bottom_right_corner = bottom_right_corner_box[2:]
print(f"bottom_right_corner = {bottom_right_corner}")

# ファイルメニューは左上なので、これでいい。
top_left_region = [max(top_left_corner[0] - 50, 0), max(top_left_corner[1] - 50, 0), \
                min(top_left_corner[0] + 300, 1920), min(top_left_corner[1] + 100, 1080)]"""
