# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

if __name__ == "__main__":
    im = Image.open('0.png')
    w, h = im.size
    print(w, h)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', 32)
    draw.text((w-w/5, h/5), '7', fill=(255,0,0), font=font)
    im.show()