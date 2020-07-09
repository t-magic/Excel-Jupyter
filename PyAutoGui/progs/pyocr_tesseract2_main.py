from PIL import Image
import sys
import os
import glob

import pyocr
import pyocr.builders

def main(dir_png, dir_txt):
    #png_file_list = sorted(os.listdir(dir_png))
    png_file_list = [x.replace('\\', '/') for x in sorted(glob.glob(dir_png + '/*.png'))]
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
            txt_filenname = os.path.basename(png_file_path).replace('.png', '') + '.txt'
            txt_file_path = dir_txt + '/' + txt_filenname
            print(txt_file_path)


            txt = tool.image_to_string(
                #Image.open('../data/test.png'),
                #Image.open('../data/ocr-test.png'),
                Image.open(png_file_path),
                lang="jpn",
                builder=pyocr.builders.TextBuilder(tesseract_layout=6)
            )
            #text_file = png_file_path.replace('.png', '') + '.txt'
            with open(txt_file_path, 'w') as f:
                f.write(txt)
            print( txt )








if __name__ == '__main__':

    print('sys.argv[1:]         : ', sys.argv[1:])
    print('type(sys.argv)   : ', type(sys.argv))
    print('len(sys.argv)    : ', len(sys.argv))
    main(sys.argv[1], sys.argv[2])

