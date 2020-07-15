#!/usr/bin/env python
# -*- coding: utf-8 -*-

# [Python, Pillowで円や四角、直線などの図形を描画 | note.nkmk.me]
# (https://note.nkmk.me/python-pillow-imagedraw/)
import glob
from PIL import Image, ImageDraw
#jpg_path_list = sorted(glob.glob("Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門_目次/*.jpg"))
jpg_path_list = sorted(glob.glob("Z:/ScanPdf/Jupyter実践入門/Jupyter実践入門/*.jpg"))

for count, jpg_path in enumerate(jpg_path_list[3:]):
    if count > 10:
        break
    im = Image.open(jpg_path)
    print(im.size)
    offset = 2
    x0 = 0
    y0 = 0
    w = im.size[0] - offset
    h = im.size[1] - offset
    draw = ImageDraw.Draw(im)
    draw.line(((x0, y0), (w, y0), (w, h), (x0, h), (x0, y0)), fill=(0, 0, 0), width = offset)
    x1 = x0 + 50
    y1 = 10 + 50
    w1 = im.size[0] - 50
    h1 = im.size[1] - 70
    draw.line(((x1, y1), (w1, y1), (w1, h1), (x1, h1), (x1, y1)), fill=(0, 255, 0), width = offset)

    # draw.polygon(((x0, y0), (w, y0), (w, h), (x0, h)), fill=(255, 255, 255), outline=(0, 0, 0))
    # draw.line(((30, 200), (130, 100), (80, 50)), fill=(255, 255, 0))
    # draw.line(((80, 200), (180, 100), (130, 50)), fill=(255, 255, 0), width=10)
    # draw.polygon(((200, 200), (300, 100), (250, 50)), fill=(255, 255, 0), outline=(0, 0, 0))
    # draw.point(((350, 200), (450, 100), (400, 50)), fill=(255, 255, 0))
    # draw.pieslice((15, 50, 140, 175), start=30, end=330, fill=(255, 255, 0))
    im.show()
    input(">> ")



#im_crop = im.crop((0, 0, w/2, h/2))
#im_crop.save('Z:/ScanPdf/test/lena_pillow_crop.jpg', quality=95)


'''(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)
(1240, 1754)'''