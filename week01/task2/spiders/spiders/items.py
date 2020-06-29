# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    film_name = scrapy.Field()
    movie_type = scrapy.Field()
    plant_date = scrapy.Field()