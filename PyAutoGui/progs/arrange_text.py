#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
[Pythonの正規表現で漢字・ひらがな・カタカナ・英数字を判定・抽出・カウント | note.nkmk.me]
(https://note.nkmk.me/python-re-regex-character-type/)

ASCII文字
>>> p = re.compile('[\u0000-\u007F]+')
>>> bool(p.fullmatch('(abc)!_(123)?'))
True
'''
import os
import re
p = p = re.compile('[\u0000-\u007F]+')

def read_a_page(filepath, prev_text_line, cont_thres_len, last_pagep, tracep = False):
    if tracep:
        print(f"prev_text_line = {prev_text_line}")
    # 直前の行の長さを求める
    prev_text_len = len(prev_text_line)
    prev_last_char_type = "ascii"
    # text = open(filepath).read()
    # 各行の長さを調べる
    #with open(filepath) as f:
    #    text_lines = f.readlines()
    text_lines = open(filepath).readlines()
    #print(text_lines)
    #len_text_line = [len(line) for line in text_lines]
    #print(len_text_line)
    #prev_len = 0

    # 確認: この時点(行)までで、prev_text_line, prev_text_len は設定されている。
    # 出力用テキスト
    output_text = prev_text_line
    output_text_list = []
    #for text_line, text_len in zip(text_lines, len_text_line):
    for count, text_line in enumerate(text_lines):
        # 直前の行の最後の文字がアスキーかどうかを判定する。
        prev_last_char_type = "a" \
            if len(prev_text_line) > 0 and bool(p.match(prev_text_line[-1])) \
            else "j"
        # 直前の行の長さが、現在の行に改行記号なしで継続させるかどうかを判定するフラグの値を設定する。
        cflag = 1 if prev_text_len >= cont_thres_len else 0
        # 直前の行の最後がアスキーかどうかを判定にはまだ入れていない。

        # 現在の行の行末の改行を取り除き、長さを求める。
        text_line = text_line.rstrip('\n')
        text_len = len(text_line)

        #new_line_or_null = "" if prev_text_len >= cont_thres_len else "\n"
        #output_text += new_line_or_null + text_line

        if prev_text_len >= cont_thres_len:
            # 直前の行の長さが閾値よりも長い場合は、
            # 現在の行との間は改行なしの継続なので
            # 直前の行をテキストバッファーに追加する。
            output_text += text_line
            #

        else:
            # 直前の行の長さが閾値よりも短い場合は、
            # 現在の行との間は改行ありなので
            # 直前までの行の内容をリストに追加する。
            # そして、テキストバッファーをクリアして、現在の行を入れます。
            output_text_list.append(output_text)
            output_text = text_line

        # 文字列の最後が「。」の場合、そこまでをフラッシュする。
        # 各行の行末が「。」の場合、フラッシュすることで、
        # 各ページの最後の行が「。」の場合、次ページに送られるのを防ぐ。
        if len(output_text) > 0 and output_text[-1] == "。":
            output_text_list.append(output_text)
            output_text = ""
            text_line = ""
            text_len = 0


        if tracep:
            print(f"{count}: {text_len}({prev_last_char_type} {cflag}): {text_line}")

        # 次に送るための準備をする
        prev_text_line = text_line
        prev_text_len = text_len

    # 最終ページの場合のフラッシュ処理
    # 念のため入れておく。
    if last_pagep:
        output_text_list.append(output_text)
        output_text = ""
    return output_text_list, prev_text_line, prev_text_len

def read_pages(filepath_list, prev_text_line, cont_thres_len, output_dir_path, tracep=False):
    for filepath_count, filepath in enumerate(filepath_list):
        last_pagep = filepath_count == len(filepath_list) - 1 # True if so
        output_text_list, prev_text_line, prev_text_len \
            = read_a_page(filepath, prev_text_line, cont_thres_len, last_pagep, tracep=tracep)
        # output_text_list = [x.replace(' ', '') for x in output_text_list]
        if tracep:
            print(f"output_text_list = {output_text_list}")
            print(f"prev_text_line = {prev_text_line}")
            print(f"prev_text_len = {prev_text_len}")

            print(f"output_dir_path + os.path.basename(filepath) = {output_dir_path + os.path.basename(filepath)}")
        with open(output_dir_path + os.path.basename(filepath), "w") as outputf:
            for count, output_text in enumerate(output_text_list):
                # 文字列の後ろから空白を削除していけば、文字の場所のインデックスは変わらない
                if tracep:
                    print(f"{count}: output_text = {output_text}")
                #if len(output_text) > 2:
                #    print(f"output_text[2] = {output_text[2]}")
                #    print(f"ord(output_text[2]) = {ord(output_text[2])}")
                output_text_list = list(output_text)
                """if count == 3:
                    print(f"len(output_text) = {len(output_text)}")"""
                for i in range(len(output_text_list) - 2, 0, -1): # 右端の一つ手前から左端から2番目まで
                    # 前後のどちらかもアスキーならば、空白を残す。
                    """if count == 3:
                        print(f"i = {i}")
                    if count == 3 and i == 1:
                        print('+' * 40)
                    #if output_text_list[i] == " ":
                        print(f"{count},{i}: {bool(p.match(output_text_list[i - 1]))} {bool(p.match(output_text_list[i + 1]))}")
                    """
                    # スペースの左右どちらかがASCII出ない場合、スペースを取り除いていい。
                    if output_text_list[i] == " " \
                            and (not(bool(p.match(output_text_list[i - 1]))) \
                                 or \
                                 not(bool(p.match(output_text_list[i + 1])))):
                        output_text_list.pop(i)
                        #print('*fire*')
                #print(f"(空白を除いた) output_text_list = {output_text_list}")
                output_text = "".join(output_text_list)
                if tracep:
                    print(f"{count}: (空白を除いた) output_text = {output_text}")
                outputf.write(output_text + "\n")
                if tracep:
                    print(f"1: filepath_count = {filepath_count}")
            """if filepath_count == len(filepath_list) - 1:   # 最後のページの場合、flushする。
                print(f"2: filepath_count = {filepath_count}")
                outputf.write(output_text + prev_text_line + "\n")
                output_text = ""
                prev_text_line = ""
                """



#filepath = "Z:/ScanKindle/PyTorch_text/p1_0025.txt"
#filepath_list = ["Z:/ScanKindle/PyTorch_text/p1_0025.txt", \
#                 "Z:/ScanKindle/PyTorch_text/p1_0026.txt"]

import glob
filepath_list = sorted(glob.glob("Z:/ScanKindle/PyTorch_text/*.txt"))
filepath_list = [x.replace("\\", "/") for x in filepath_list]
#print(filepath_list[:10])

output_dir_path = "Z:/ScanKindle/PyTorch_clean_text/"
prev_text_line = ""
cont_thres_len = 65

read_pages(filepath_list, prev_text_line, cont_thres_len, output_dir_path, tracep=False)
