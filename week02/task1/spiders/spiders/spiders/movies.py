import scrapy
from spiders.items import MaoyanmovieItem
from scrapy import Selector
import re

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        try:
            url = 'https://maoyan.com/films?showType=3'
            yield scrapy.Request(url=url, callback=self.parse)
        except Exception as e:
            self.logger.error(e)

    def parse(self, response):
        try:
            movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
            for movie in movies[:10]:
                relative_url = movie.xpath('./a/@href').extract_first().strip()
                movie_url = 'https://maoyan.com' + relative_url
                yield scrapy.Request(url=movie_url, callback=self.parse2)
        except Exception as e:
            self.logger.error(e)

    # 解析具体页面
    def parse2(self, response):
        try:
            movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
            item = MaoyanmovieItem()
            film_name = movie.xpath('./h1/text()').extract_first().strip()
            item['film_name'] = film_name

            film_types = movie.xpath('./ul/li[1]/*/text()').extract()
            item['movie_type'] = ','.join(film_types)

            plant_date = movie.xpath('./ul/li[3]/text()').extract_first().strip()
            plant_date = re.sub(r'[^\d-]', "", plant_date)
            item['plant_date'] = plant_date

            yield item

        except Exception as e:
            self.logger.error(e)
