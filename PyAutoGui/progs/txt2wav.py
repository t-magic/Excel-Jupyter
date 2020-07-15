#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
以下のプログラムをまとめて作成する。
(1) file_to_clip.py
    テキストファイルを読み、その内容を「かんたん! AITalk」のテキストペインに貼り付ける。

(2) click_on_play_button.py
    「かんたん! AITalk」の再生ボタンをクリックする。これは実行しなくてもいい。

(3) click_on_wave_file_save.py
    ファイルメニューをクリックし、WAVファイルで保存する。

まとめる際に、アプリの位置を取得する関数を使用する。

'''

import pyperclip
import pyautogui

import time
import os
import datetime
import glob

def get_appli_region(topLeftCorner_png, bottomRightCorner_png, tracep = True):
    '''
    アプリケーションのGUIの箱座標(左, 上, 右, 下)を返す。
    :param topLeftCorner_png: 左上隅に探し出すべき画像
    :param bottomRightCorner_png: 右下隅に探し出すべき画像
    :param tracep: トレース情報を表示するかどうか
    :return: アプリのGUIの矩形の左、上、右、下の座標
    '''

    # 左上隅の座標を求める。
    top_left_corner_box = pyautogui.locateOnScreen(topLeftCorner_png, grayscale=True, confidence=0.9)
    top_left_corner = top_left_corner_box[0:2]
    if tracep:
        print(f"top_left_corner = {top_left_corner}")

    # 右下隅の座標を求める。
    bottom_right_corner_box = pyautogui.locateOnScreen(bottomRightCorner_png, grayscale = True, confidence = 0.9)
    print(f"bottom_right_corner_box = {bottom_right_corner_box}")
    # bottom_right_corner_box = Box(left=669, top=805, width=230, height=77)
    try:
        bottom_right_corner = [bottom_right_corner_box[0] + bottom_right_corner_box[2], \
                               bottom_right_corner_box[1] + bottom_right_corner_box[3]]
    except:
        print('「かんたん! AITalk」のGUIが見つかりません')

    if tracep:
        print(f"bottom_right_corner = {bottom_right_corner}")

    # アプリケーションのGUIの箱座標(左, 上, 右, 下)を返す。
    return [top_left_corner[0], top_left_corner[1], bottom_right_corner[0], bottom_right_corner[1]]

def click_to_save_wav_file(wav_file_path, appli_region):
    '''
    現在のテキストペインにあるテキストを保存する
    :param wav_file_path: 保存するWAVファイルのファイルパス
    :param appli_region: 「かんたん! AITalk」のGUIの矩形の
    :return: 左、上、右、下の座標
    '''
    # アプリのGUIの左上隅と右下隅の画像を入力して、その二つで作るアプリの矩形を得る。
    #appli_region = get_appli_region("../data/png/AITalk_TopLeftCorner.png", \
    #                                "../data/png/AITalk_BottomRightCorner.png")
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

def txt2wav(txt_file_path, wav_file_path, appli_region, text_pastep = True, talkp = False, save_wavp = True):
    # 1. アプリケーションのGUIの箱座標(左, 上, 右, 下)を返す。
    #appli_region = get_appli_region("../data/png/AITalk_TopLeftCorner.png", \
    #                                "../data/png/AITalk_BottomRightCorner.png")
    # まわりにマージンをつけた矩形
    appli_region_with_margin =  [max(appli_region[0] - 50, 0), max(appli_region[1] - 50, 0), \
                       min(appli_region[2] + 50, 1920), min(appli_region[3] + 50, 1080)]

    # 1. テキストファイルを読み、その内容を「かんたん! AITalk」のテキストペインに貼り付ける。
    if text_pastep:
        # 1-1. 左上から、右100、下100移動した場所をクリックすることで、テキストペインを選ぶ
        x, y = [appli_region[0] + 100, appli_region[1] + 100]
        pyautogui.click(x, y)

        # 1-2. テキスト全体を選んで削除する
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'x')
        #print(pyperclip.paste())

        # 1-3. ファイルを読み込んで、クリップボードに送り込む。
        # 1-3-1. 中身が空の場合は、そこで引き返す。
        contents = open(txt_file_path).read()
        if len(contents.strip()) <= 1:
            return
        pyperclip.copy(contents)

        # 1-4. テキストをテキストペインにペーストする
        pyautogui.hotkey('ctrl', 'v')

    # 2. 「かんたん! AITalk」の再生ボタンをクリックする。
    if talkp:
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen("../data/png/AITalk_Play.png", region = appli_region_with_margin)
                break
            except:
                pass
        print(x, y)
        pyautogui.click(x, y)
        # マウスポインターが再生ボタン上にあると、読み上げが終わっても先に進まないので、右上にずらす
        pyautogui.move(100, -100)
        while True:
            time.sleep(5)
            print('.', end="")
            try:
                # プレイボタンが戻ってきた。
                ret = pyautogui.locateOnScreen("../data/png/AITalk_Play.png", region = appli_region_with_margin)
                print(f"ret = {ret}")
                if ret != None:
                    break
            except:
                pass
        print('finish to talk: ポインターが再生ボタンの上にあると先にすすめません。')

    # 3. 表示されているテキストを読み上げて、WAVファイルとして保存する。
    if save_wavp:
        #wav_file_path = r'Z:\ScanKindle\PyTorch_clean_text_voice\test.wav'
        click_to_save_wav_file(wav_file_path, appli_region)

        #WAVファイルができたことを確認する。さもないと、次の試行が重なって(追い越して)しまう。
        while True:
            if os.path.exists(wav_file_path):
                break
            else:
                time.sleep(1)

def texts2wavs(txt_file_path_list, wav_dir_path, text_pastep=True, talkp=True, save_wavp=True):
    appli_region = get_appli_region("../data/png/AITalk_TopLeftCorner.png", \
                                    "../data/png/AITalk_BottomRightCorner.png")
    for txt_file_path in txt_file_path_list:
        #pyautogui.alert(text=f"{txt_file_path}の処理を始めます。", title='お知らせ', button='OK')
        #txt_file_basename = os.path.basename(txt_file_path)
        wav_file_basename = os.path.splitext(os.path.basename(txt_file_path))[0] + '.wav'
        wav_file_path = wav_dir_path + wav_file_basename
        print(wav_file_path)

        # 実行!!
        txt2wav(txt_file_path, wav_file_path, appli_region, text_pastep=text_pastep, talkp=talkp, save_wavp=save_wavp)
        time.sleep(1)
        #print(os.path.splitext(os.path.basename(txt_file_path)))
        # ('p1_0009', '.txt')

        #print(wav_file_basename)
        # p1_0009.wav
    pyautogui.alert(text="終了しました。", title = 'お知らせ', button = 'OK')


# メイン
#txt_file_path = "Z:/ScanKindle/PyTorch_clean_text/p1_0025.txt"
# 以下は、WindowsのGUIで入れる文字列なので、Pythonで使えるスラッシュ(/)は使えない
#wav_file_path = r'Z:\ScanKindle\PyTorch_clean_text_voice\test.wav'
#txt2wav(txt_file_path, wav_file_path, text_pastep = False, talkp = True, save_wavp = False)
#txt2wav(txt_file_path, wav_file_path, text_pastep = False, talkp = True, save_wavp = True)

wav_dir_path = 'Z:\\ScanKindle\\PyTorch_clean_text_voice\\'

# WAVフォルダーが空でない場合は中断する。
if os.listdir(wav_dir_path) != []:
    pyautogui.alert(text="WAVファイルを出力するフォルダーが空ではありません。空にしてから再度実行してください。", title = 'お知らせ', button = 'OK')
    #exit()

# お知らせの表示
ret = pyautogui.alert(text = "かんたん! AITalkは、作業中、全体が表示されるようにしておいてください。", title = "お知らせ", button = "OK")
print(f"ret = {ret}")
# ret = OK
#time.sleep(5)

txt_file_path_list = [x.replace('\\', '/') for x in sorted(glob.glob("Z:/ScanKindle/PyTorch_clean_text/*.txt"))]
print(txt_file_path_list[:10])

txt_file_path_list = txt_file_path_list[96:]
# 実行!!
#texts2wavs(txt_file_path_list, wav_dir_path, text_pastep=True, talkp=True, save_wavp=True)
texts2wavs(txt_file_path_list, wav_dir_path, text_pastep=True, talkp=False, save_wavp=True)
