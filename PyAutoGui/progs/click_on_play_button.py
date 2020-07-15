#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip
import pyautogui

import time
import os
import datetime

time.sleep(5)

print(pyautogui.locateOnScreen("../data/png/AITalk_Play.png", region = (930, 530, 1140, 680)))
print(pyautogui.locateCenterOnScreen("../data/png/AITalk_Play.png", region = (930, 530, 1140, 680)))
x, y = pyautogui.locateCenterOnScreen("../data/png/AITalk_Play.png", region = (930, 530, 1140, 680))
print(x, y)
pyautogui.click(x, y)
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
print('finish')