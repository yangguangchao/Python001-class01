# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os

#数据保存到csv中，字符集为utf-8
class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        f = open('./movies.csv', 'a+', encoding='utf8')
        writer = csv.writer(f)
        writer.writerow((item['film_name'], item['movie_type'], item['plant_date']))
        f.close()
        return item
