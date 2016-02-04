#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 16:07:22
# @Last Modified by:   lutz
# @Last Modified time: 2016-02-03 17:32:56


class Message:

	def __init__(self, text):
		self.text = text

		#add 7 trailing spaces
		self.text += "       "

		self.textPosition = 0

	def hasEnded(self):
		return self.textPosition >= len(self.text)

	def getNextCharacter(self):
		char = list(self.text)[self.textPosition]
		self.textPosition = self.textPosition + 1
		return char


class PrintFeed:

	def __init__(self, numberOfColumns):

		self.columns = [None] * numberOfColumns # column array
		self.queue = [] # message queue

	# adds message to queue
	def addMessage(self,text):
		self.queue.append(Message(text))

	def getNextColumn(self):
		characters = []

		for msg in self.columns:
			if not (msg is None):
				characters.append(msg.getNextCharacter());
			else:
				characters.append(None)

		# clean up empty messages and assign queue
		self.__cleanMessages()
		self.__assignColumns()

		return characters;

	# assigns messages to columns
	def __assignColumns(self):
		for i in xrange(len(self.columns)):
			msg = self.columns[i]
			if (msg is None) and (len(self.queue) > 0):
				self.columns[i] = self.queue.pop(0)

	# cleans emtpy messages
	def __cleanMessages(self):
		for i in xrange(len(self.columns)):
			msg = self.columns[i]
			if not (msg is None) and (msg.hasEnded()):
				self.columns[i] = None;
