from PIL import Image
import sys
import os
import glob

import pyocr
import pyocr.builders

def main(dir_img, dir_txt, img_type, left_offset, top_offset, right_offset, bottom_offset):
    #png_file_list = sorted(os.listdir(dir_img))
    png_file_list = [x.replace('\\', '/') for x in sorted(glob.glob(dir_img + '/*.' + img_type))]
        # img_type: png, jpg
    print(png_file_list[:10])

    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]
    #print("Will use tool '%s'" % (tool.get_name()))
    # Ex: Will use tool 'libtesseract'

    langs = tool.get_available_languages()
    #print("Available languages: %s" % ", ".join(langs))
    #lang = langs[0]
    #print("Will use lang '%s'" % (lang))

    for count, png_file_path in enumerate(png_file_list):
        if True:  # count == 20:
            print(png_file_path)
            txt_filenname = os.path.basename(png_file_path).replace('.' + img_type, '') + '.txt'
            txt_file_path = dir_txt + '/' + txt_filenname
            print(txt_file_path)

            # イメージファイルを読み込む
            im = Image.open(png_file_path)
            txt = tool.image_to_string(
                #Image.open('../data/test.png'),
                #Image.open('../data/ocr-test.png'),
                im,
                lang="jpn",
                builder=pyocr.builders.TextBuilder(tesseract_layout=6)
            )
            #text_file = png_file_path.replace('.png', '') + '.txt'
            with open(txt_file_path, 'w') as f:
                f.write(txt)
            print( txt )

# sys.argv[1]: Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門_目次/jpg
# sys.argv[2]: Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門_目次/text
# sys.argv[3]: jpg
# sys.argv[4]: 50  (left offset to right)   矩形の左上端の位置から、右に移動
# sys.argv[5]: 50  (top offset to bottom)   矩形の左上端の位置から、下に移動
# sys.argv[6]: 50  (right offset to left)   矩形の右下端の位置から、右に移動
# sys.argv[7]: 50  (bottom offset to top)   矩形の右下端の位置から、上に移動

if __name__ == '__main__':
    #dir_img = "Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門_目次/jpg"
    #dir_txt = "Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門_目次/text"

    dir_img = "Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門/jpg"
    dir_txt = "Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門/text"
    #print('sys.argv[1:]         : ', sys.argv[1:])
    #print('type(sys.argv)   : ', type(sys.argv))
    #print('len(sys.argv)    : ', len(sys.argv))
    #main(sys.argv[1], sys.argv[2])
    # 四つのoffsetは、test_page_size.pyで試行錯誤して得た。
    main(dir_img, dir_txt, "jpg", 50, 50, 50, 70)

