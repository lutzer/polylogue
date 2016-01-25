#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-25 16:17:08
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-25 17:09:45

from PIL import Image
import json

class FontRenderer:

	def __init__(self, imagePath, jsonPath):

		# load image
		img = Image.open(imagePath) 
		# make background white
		bg = Image.new("RGB", img.size, (255, 255, 255))
		bg.paste(img, mask=img.split()[3]) # 3 is the alpha channel
		self.symbolImage = bg;

		# load font data
		with open(jsonPath) as data_file:    
		    self.charTable = json.load(data_file)

	def getCharacterImage(self, character):

		# get char from table
		charData = self.charTable['chars'][str(ord(character))]

		# crop sybol img
		return self.symbolImage.crop([
			charData['x'], 
			charData['y'], 
			charData['x'] + charData['width'],
			charData['y'] + charData['height'],
		])


font = FontRenderer("inconsolata.png", "inconsolata.json");

img = font.getCharacterImage('c')
img.show();