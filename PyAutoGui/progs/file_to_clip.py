#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip
import pyautogui

import time
import os
import datetime

time.sleep(5)
# ファイルを読み込んで、クリップボードに送り込む。
pyperclip.copy(open("Z:/ScanKindle/PyTorch_clean_text/p1_0025.txt").read())
#print(pyperclip.paste())
pyautogui.hotkey('ctrl', 'v')
