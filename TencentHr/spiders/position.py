#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Flynn on 2017-12-25 23:29

import scrapy
from TencentHr.items import PositionItem
import time


class PositionSpider(scrapy.Spider):
	name = 'position'
	allowed_domains = ['hr.tencent.com']
	url = 'http://hr.tencent.com/position.php?keywords=&lid=0&start={}'
	start_urls = [url.format(str(0))]

	start_position = 0

	def parse(self, response):
		print('start_position = ', self.start_position)
		all = response.xpath('// *[ @ id = "position"] / div[1] / table / tr')
		for item in all:
			job_name = item.xpath('./td[1]/a/text()').extract_first()
			job_type = item.xpath('./td[2]/text()').extract_first()
			job_number = item.xpath('./td[3]/text()').extract_first()
			job_city = item.xpath('./td[4]/text()').extract_first()
			job_time = item.xpath('./td[5]/text()').extract_first()

			items = PositionItem()
			items['job_name'] = job_name
			items['job_type'] = job_type
			items['job_number'] = job_number
			items['job_city'] = job_city
			items['job_time'] = job_time

			# print(items)

			yield items

		if self.start_position <= 2690:
			self.start_position += 10
		time.sleep(3)
		yield scrapy.Request(self.url.format(str(self.start_position)), callback=self.parse)
