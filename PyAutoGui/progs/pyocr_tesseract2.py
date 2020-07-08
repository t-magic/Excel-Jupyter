from PIL import Image
import sys

import pyocr
import pyocr.builders

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


txt = tool.image_to_string(
    #Image.open('../data/test.png'),
    #Image.open('../data/ocr-test.png'),
    Image.open('../data/book1/picture_0003.png'),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print( txt )