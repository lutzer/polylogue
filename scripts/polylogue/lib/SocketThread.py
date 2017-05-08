#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 17:02:11
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-27 11:42:54

from __future__ import with_statement
from socketIO_client import SocketIO
import time
import logging
from threading import Thread,Lock
from pprint import pformat

logger = logging.getLogger(__name__)

socketThread = None

class Sockethread(Thread):

	def __init__(self,address,port):
		self.socket = socket = SocketIO(address,port, verify=False)
		self.socket.on('submission:new', self.onNewSubmission)

		self.lock = Lock()
		self.queue = []

		self.running = True
		Thread.__init__(self)

	def run(self):
		logger.info('started Socket Thread.');
		self.socket.on('submission:new', self.onNewSubmission)
		while (self.running):
			self.socket.wait(seconds=1); #TODO: test if this is ok

	def stop(self):
		logger.info('stopped Socket Thread.')
		self.running = False

	def onNewSubmission(self,data):
		logger.info("Received new submission: " + pformat(data))

		# add submission to queue
		with self.lock:
			self.queue.append(data)

	# returns copy of queue and clears it
	def getQueue(self):
		with self.lock:
			messages = list(self.queue)
			self.queue[:] = [] #clear queue
			return messages

			