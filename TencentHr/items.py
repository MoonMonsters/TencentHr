# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencenthrItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	pass


class PositionItem(scrapy.Item):
	# 工作名称
	job_name = scrapy.Field()
	# 工作类型
	job_type = scrapy.Field()
	# 招聘人数
	job_number = scrapy.Field()
	# 所在城市
	job_city = scrapy.Field()
	# 发布时间
	job_time = scrapy.Field()