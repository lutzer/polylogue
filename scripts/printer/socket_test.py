#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 12:40:53
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-26 17:14:58

from __future__ import with_statement
from socketIO_client import SocketIO
import time
from threading import Thread,Lock

from lib.SocketThread import *

socketThread = None

def init():
	global socketThread 
	socketThread = Sockethread('localhost',8081)
	socketThread.start()

# check the socketThread if there are any new messages received
def loop():
	global socketThread
	queue = socketThread.getQueue();
	for submission in queue:
		print submission
	time.sleep(5)

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