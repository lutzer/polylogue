#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-25 16:17:08
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-25 19:04:52

from lib.FontRenderer import *
from PIL import Image


font = FontRenderer("font/inconsolata.png", "font/inconsolata.json", (200,200) );

img = font.getCharacterImage('P')
#img = img.rotate(90,0,True)
img = font.makeBgWhite(img)

bg = Image.new("RGB", (img.size[0], 500), (255, 255, 255))
bg.paste(img, box=(0, (500 - font.fontSize()) /2))

bg.show();