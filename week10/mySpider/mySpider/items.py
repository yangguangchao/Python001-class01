# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class SmzdmItem(Item):
    title = Field()
    price = Field()
    detail_url = Field()
    comment = Field()
    comment_date = Field()
