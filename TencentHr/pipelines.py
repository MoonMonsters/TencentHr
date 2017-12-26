# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from TencentHr.db.mongodb import MongoTencent


class TencenthrPipeline(object):
	def process_item(self, item, spider):
		return item


class PositionPipeline(object):
	def __init__(self):
		# 数据库对象
		self.mongo = MongoTencent()

	def process_item(self, item, spider):
		# 过滤空白数据
		if item['job_name'] and item['job_type'] and item['job_city'] and item['job_number'] and item['job_time']:
			print(dict(item))
			# 存入数据库
			self.mongo.insert(dict(item))
