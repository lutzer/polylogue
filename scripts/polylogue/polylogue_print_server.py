#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 12:40:53
# @Last Modified by:   lutz
# @Last Modified time: 2016-02-04 17:23:32

from __future__ import with_statement
from socketIO_client import SocketIO
import time
import logging
from threading import Thread,Lock
from PIL import Image
from pprint import pformat
import serial.tools.list_ports

from lib.Adafruit_Thermal import *
from lib.FontRenderer import *
from lib.SocketThread import *
from lib.PrintFeed import *

# Debug options
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('logs/letterbox_service.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 

FONT_WIDTH = 39 #32 px monspace font

PRINTER_PAPER_WIDTH = 300 # in pixels
PRINTER_PAPER_MARGIN = 75 # distance to the border of the printer
PRINTER_COLUMNS = 3 # number of characters in one column

socketThread = None
printFeed = None
printer = None
fontRenderer = None

def init():
   global socketThread, printFeed, fontRenderer, printer

   # connect printer
   # printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
   printer = Adafruit_Thermal("/dev/tty.Bluetooth-Incoming-Port", 19200, timeout=5)
   
   
   #load font
   fontRenderer = FontRenderer('font/cutivemono.png','font/cutivemono.json',FONT_WIDTH)  

   # init print feed with 3 lines
   printFeed = PrintFeed(PRINTER_COLUMNS)

   # start socket connection
   socketThread = Sockethread('localhost',8081)
   socketThread.start()

   logger.info("Polyloge print server started.")

# check the socketThread if there are any new messages received
def loop():
   global socketThread, printFeed

   # get new messages from node server and add messaged to queue
   queue = socketThread.getQueue()
   for submission in queue:
      printFeed.addMessage(removeNonAsciChars(submission['data']['message']))

   col = printFeed.getNextColumn()

   if any(col):
      sendToPrinter(col)
   else:
      time.sleep(1)

def stop():
   global socketThread
   socketThread.stop()

def removeNonAsciChars(text):
   return ''.join([i if ord(i) < 128 else ' ' for i in text])

def sendToPrinter(column):
   global printer, fontRenderer
   logger.info('Printing column:' + pformat(column));

   fontSize = fontRenderer.fontSize()
   columnStart = (PRINTER_PAPER_WIDTH - PRINTER_PAPER_MARGIN - fontSize)/ (PRINTER_COLUMNS-1)

   # create image that fills the whole column
   img = Image.new("RGB", (PRINTER_PAPER_WIDTH, FONT_WIDTH), (255, 255, 255))

   # print messsage character by character
   for i,character in enumerate(column):

      if not (character is None):

         symbol = fontRenderer.getCharacterImage(character)
         symbol = symbol.rotate(270, 0, True)
         symbol = fontRenderer.makeBgWhite(symbol)

         img.paste(symbol, box=(PRINTER_PAPER_MARGIN + columnStart * i, 0))

   # send img to printer device
   #mg.show()
   #time.sleep(10)
   printer.wake()
   printer.printImage(img)
   printer.sleep()

# start main loop
init()
try:
   while True:
      loop()
except KeyboardInterrupt:
   print("# program loop interrupted")
finally:
   stop()