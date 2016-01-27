#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 12:40:53
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-27 13:59:57

from __future__ import with_statement
from socketIO_client import SocketIO
import time
from threading import Thread,Lock

from ..lib.SocketThread import *
from ..lib.PrintFeed import *

socketThread = None
printFeed = None

def init():
	global socketThread, printFeed 
	printFeed = PrintFeed(3)

	# start socket connection
	socketThread = Sockethread('localhost',8081)
	socketThread.start()

# check the socketThread if there are any new messages received
def loop():
	global socketThread, printFeed
	queue = socketThread.getQueue()
	for submission in queue:
		printFeed.addMessage(submission['data']['message'])

	col = printFeed.getNextColumn()

	if any(col):
		print col
	else:
		print "empty columns"
		
	time.sleep(1.5)

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