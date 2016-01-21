
'''
	Polylogue Printing Script
	@author Lutz Reiter, Design Research Lab, UDK Berlin
	@year 2015
'''

#!/usr/bin/python

from lib.Adafruit_Thermal import *
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

   # print messsage
   printer.println(message)

   printer.sleep();

   print 'done.'

if __name__ == "__main__":
   main(sys.argv[1:])

