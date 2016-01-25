#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-25 17:10:20
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-25 17:14:36

# this script will take a bitmap file and crop the symbols from it,
# corresponding to the values stored in the json file.
# The bitmap font was made using spriteFontBuilder for Mac,
# the .fnt was converted by this script: 
# https://github.com/playcanvas/fonts/blob/master/fnt_to_json.py

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