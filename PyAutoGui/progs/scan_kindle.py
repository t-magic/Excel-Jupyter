#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import os
import datetime
#########################
# 変数定義
# (環境に応じて変更する)
#########################

# ページ数
page = 5
# 取得範囲：左上座標
x1, y1 = 428, 110
# 取得範囲：右下座様
x2, y2 = 1049, 955
# スクショ間隔(秒)
span = 1
# 出力フォルダ頭文字
h_foldername = "output"
# 出力ファイル頭文字
h_filename = "picture"


#########################
# スクリーンショット取得処理
#########################

# 待機時間５秒
# (この間にスクショを取得するウィンドウをアクティブにする)
time.sleep(5)

# 出力フォルダ作成(フォルダ名：頭文字_年月日時分秒)
folder_name = h_foldername + "_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
os.mkdir(folder_name)

# ページ数分スクリーンショットをとる
for p in range(page):
    # 出力ファイル名(頭文字_連番.png)
    out_filename = h_filename + "_" + str(p+1).zfill(4) + '.png'
    # スクリーンショット取得・保存処理
    # キャプチャ範囲： 左上のx座標, 左上のy座標, 幅, 高さ
    s = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
    # 出力パス： 出力フォルダ名 / 出力ファイル名
    s.save(folder_name + '/' + out_filename)
    # 右矢印キー押下
    pyautogui.keyDown('right')
    # 次のスクリーンショットまで待機
    time.sleep(span)
