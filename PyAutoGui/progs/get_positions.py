#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [【Python】pyautoguiを使ってKindle書籍を自動でスクショするツールを作ってみた！ | 都会のエレキベア]
# (https://elekibear.com/

# ポインター位置の座標を確認するにはMPPUtilityを使用する。
# C:\Users\tateno\Downloads\MPPUtility119\MPPUtility.exe

import pyautogui
import time

#########################
# キャプチャ座標計測
#########################

# 左上座標を取得
print('キャプチャ範囲の左上座標にマウスカーソルを合わせるでやんす')
time.sleep(3)
print('左上座標：' + str(pyautogui.position()))

# １秒待機
time.sleep(1)

# 右下座標を取得
print('キャプチャ範囲の右下座標にマウスカーソルを合わせるでやんす')
time.sleep(3)
print('右下座標：' + str(pyautogui.position()))