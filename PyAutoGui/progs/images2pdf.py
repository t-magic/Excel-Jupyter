#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [kindle 自動スクショ 連続 · Issue #751 · t-magic/keep2git]
# (https://github.com/t-magic/keep2git/issues/751)

# [pythonで複数画像をPDFファイルに変換する - Qiita]
# (https://qiita.com/meznat/items/31d947ed4826350fd9fa)

# conda activate py37_PyAutoGui
# conda install -c conda-forge img2pdf
# conda install -c conda-forge pathlib

import img2pdf
from pathlib import Path

#単処理
def ImageToPdf(outputpath, imagepath):
    '''
    outputpath: pathlib.Path()
    imagepath: pathlib.Path()
    '''
    lists = list(imagepath.glob("**/*"))#単フォルダ内を検索
    print(f'lists = {lists}')
    #pdfを作成
    with open(outputpath,"wb") as f:
        #jpg,pngファイルだけpdfに結合
        #Pathlib.WindowsPath()をstring型に変換しないとエラー
        f.write(img2pdf.convert([str(i) for i in lists if i.match("*.jpg") or i.match("*.png")]))
    print(outputpath.name + " :Done")

#複数フォルダをループ処理する
def main():
    #作業フォルダ
    base_path = r"output_0"
    #作業フォルダ内のディレクトリだけを抽出する
    glob = Path(base_path).glob("*")
    print(f'glob = {glob}')
    imagefolderlist = list([item for item in list(glob) if item.is_dir()])
    #outputpathに指定ディレクトリと同名を指定する
    outputpathlist = list([item.with_name(item.name + ".pdf") for item in imagefolderlist])
    #ループ処理を行う
    for outputpath,imagepath in zip(outputpathlist,imagefolderlist):
        try:
            print(f'outputpath = {outputpath}, imagepath = {imagepath}')
            ImageToPdf(outputpath,imagepath)
        except:
            pass

main()