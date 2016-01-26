#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-21 14:58:30
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-25 19:41:16

# This script sends a message to the adafruit thermal printer.
# It prints the message vertically on the paper roll.

#!/usr/bin/python

from lib.Adafruit_Thermal import *
from lib.FontRenderer import *
import sys, getopt
from PIL import Image

PRINTER_WIDTH_PIXELS = 384 # in pixels

# read arguments
def main(argv):
   try:
      opts, args = getopt.getopt(argv,"m:",["message="])
   except getopt.GetoptError:
      print 'polylogue.py -m <message>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'polylogue.py -m <message>'
         sys.exit()
      if opt in ("-m", "--message"):
         sendToPrinter(arg)

# prints message on printer
def sendToPrinter(message):

   print 'Printing message:', message

   printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
   printer.wake()

   font = FontRenderer('font/inconsolata.png','font/inconsolata.json') 

   # print messsage character by character
   for character in list(message):

      symbol = font.getCharacterImage(character)
      symbol = symbol.rotate(270,0,True)
      symbol = font.makeBgWhite(symbol)

      # offset rotated character
      #img = Image.new("RGB", (PRINTER_WIDTH_PIXELS, symbol.size[0]), (255, 255, 255))
      #img.paste(symbol, box=(( PRINTER_WIDTH_PIXELS - font.fontSize() ) / 2, 0))

      printer.printImage(symbol)

   #printer.println(message)

   # give out some paper
   printer.feed(3)

   printer.sleep()

   print 'done.'

if __name__ == "__main__":
   main(sys.argv[1:])

