#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyautogui
import time
import os
import datetime



def main(page, x1, y1, x2, y2, span, h_foldername, h_filename):
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


import sys

if __name__ == '__main__':

    print('sys.argv[1:]         : ', sys.argv[1:])
    print('type(sys.argv)   : ', type(sys.argv))
    print('len(sys.argv)    : ', len(sys.argv))



    #########################
    # 変数定義
    # (環境に応じて変更する)
    #########################

    # scan_kindle_main.py 5 428 110 1049 955 1 ../data/books picture

    # ページ数
    page = int(sys.argv[1])
    # 取得範囲：左上座標
    x1, y1 = int(sys.argv[2]), int(sys.argv[3])
    # 取得範囲：右下座様
    x2, y2 = int(sys.argv[4]), int(sys.argv[5])
    # スクショ間隔(秒)
    span = int(sys.argv[6])
    # 出力フォルダ頭文字
    h_foldername = sys.argv[7]
    # 出力ファイル頭文字
    h_filename = sys.argv[8]

    print("Start if __name__ == '__main__'")
    print('call func()')
    main(page, x1, y1, x2, y2, span, h_foldername, h_filename)