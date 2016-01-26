#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 12:40:53
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-26 17:43:29

from __future__ import with_statement
from socketIO_client import SocketIO
import time
from threading import Thread,Lock

from lib.SocketThread import *
from lib.PrintFeed import *

socketThread = None
printFeed = None

def init():
	global socketThread, printFeed 
	socketThread = Sockethread('localhost',8081)
	socketThread.start()
	printFeed = PrintFeed(3,384)

# check the socketThread if there are any new messages received
def loop():
	global socketThread, printFeed
	queue = socketThread.getQueue()
	socketThread.clearQueue()
	for submission in queue:
		printFeed.addMessage(submission['data']['message'])
	column = printFeed.getNextColumn()
	print column
	time.sleep(2)

def stop():
	global socketThread
	socketThread.stop()

# start main loop
init()
try:
	while True:
		loop()
except KeyboardInterrupt:
	print("# program loop interrupted")
finally:
	stop()