#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-21 14:58:30
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-25 17:18:15

# This script sends a message to the adafruit thermal printer.
# It prints the message vertically on the paper roll.

#!/usr/bin/python

from lib.Adafruit_Thermal import *
from lib.FontRenderer import *
import sys, getopt

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
      printer.printImage(font.getCharacterImage(character))

   #printer.println(message)

   printer.sleep();

   print 'done.'

if __name__ == "__main__":
   main(sys.argv[1:])

