#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2017-12-25 23:29

import scrapy
from TencentHr.items import PositionItem
import time


class PositionSpider(scrapy.Spider):
	# 爬虫名称
	name = 'position'
	# 允许抓取范围，注意：不要添加http\https
	allowed_domains = ['hr.tencent.com']
	url = 'http://hr.tencent.com/position.php?keywords=&lid=0&start={}'
	start_urls = [url.format(str(0))]

	start_position = 0

	def parse(self, response):
		# print('start_position = ', self.start_position)
		# 爬取每一页的所有数据，使用xpath方式提取数据的共同前缀
		all = response.xpath('// *[ @ id = "position"] / div[1] / table / tr')
		for item in all:
			# 工作名称
			job_name = item.xpath('./td[1]/a/text()').extract_first()
			# 工作类型
			job_type = item.xpath('./td[2]/text()').extract_first()
			# 招聘人数
			job_number = item.xpath('./td[3]/text()').extract_first()
			# 工作城市
			job_city = item.xpath('./td[4]/text()').extract_first()
			# 发布时间
			job_time = item.xpath('./td[5]/text()').extract_first()

			items = PositionItem()
			items['job_name'] = job_name
			items['job_type'] = job_type
			items['job_number'] = job_number
			items['job_city'] = job_city
			items['job_time'] = job_time

			# print(items)

			yield items

		# 限制抓取最大数
		if self.start_position <= 2690:
			self.start_position += 10
		# 延时
		time.sleep(3)
		# 抓取下一页的数据
		yield scrapy.Request(self.url.format(str(self.start_position)), callback=self.parse)
