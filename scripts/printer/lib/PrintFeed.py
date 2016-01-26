#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lutz Reiter, Design Research Lab, Universität der Künste Berlin
# @Date:   2016-01-26 16:07:22
# @Last Modified by:   lutz
# @Last Modified time: 2016-01-26 17:47:02


class Message:

	def __init__(self, text):
		self.text = text
		self.textPosition = 0

	def hasEnded(self):
		return self.textPosition >= len(self.text)

	def getNextCharacter(self):
		char = list(self.text)[self.textPosition]
		self.textPosition = self.textPosition + 1
		return char

class PrintFeed:

	def __init__(self, numberOflines, sheetHeight):
		self.numberOflines = numberOflines
		self.sheetHeight = sheetHeight

		self.messages = []

	def addMessage(self,text):
		self.messages.append(Message(text))

	def getNextColumn(self):
		characters = []
		for msg in self.messages:
			if not (msg.hasEnded()):
				characters.append(msg.getNextCharacter());

		self.__cleanMessages()
		return characters;

	def __cleanMessages(self):
		for msg in self.messages:
			if (msg.hasEnded()):
				self.messages.remove(msg)
