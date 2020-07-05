# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import csv
import os

class MaoyanmoviePipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'ygc',
                       database = 'test',
                       charset = 'utf8mb4')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        data = [item['film_name'], item['movie_type'], item['plant_date']]
        self.cursor.execute('INSERT INTO maoyan_movies (name,type,plant_date) values(%s,%s,%s)', data)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
