#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2017-12-26 0:06

from pymongo import MongoClient


class MongoTencent(object):
	def __init__(self):
		self.client = MongoClient('localhost', 27017)
		self.db = self.client['tencent']
		self.table = self.db['position']

	def insert(self, data=None):
		self.table.insert_one(data)