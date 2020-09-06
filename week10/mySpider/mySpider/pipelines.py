# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql

class SmzdmPipeline(object):
    def __init__(self, host, port, user, password, database, table, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.charset = charset

    @classmethod
    def from_settings(cls, settings):
        return cls(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            database=settings['MYSQL_DATABASE'],
            table=settings['MYSQL_TABLE'],
            charset=settings['MYSQL_CHARSET'],
        )


    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        data = [item['title'], item['price'], item['detail_url'],
                item['comment'], item['comment_date']]
        self.cursor.execute('INSERT INTO %s' % self.table +
                            '(title,price,detail_url,comment,comment_date) values(%s,%s,%s,%s,%s)', data)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
