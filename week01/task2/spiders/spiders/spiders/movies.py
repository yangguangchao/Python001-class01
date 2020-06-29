import scrapy
from spiders.items import MaoyanmovieItem
from scrapy import Selector
import re

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = MoviesSpider.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)

    #解析电影url
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies[:10]:
            relative_url = movie.xpath('./a/@href').extract_first().strip()
            movie_url = 'https://maoyan.com' + relative_url
            yield scrapy.Request(url=movie_url, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):
        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        item = MaoyanmovieItem()
        film_name = movie.xpath('./h1/text()').extract_first().strip()
        item['film_name'] = film_name

        movie_type = movie.xpath('./ul/li[1]/*/text()').extract()
        item['movie_type'] = ','.join(movie_type)

        plant_date = movie.xpath('./ul/li[3]/text()').extract_first().strip()
        plant_date = re.search(r'\d{4}-\d{2}-\d{2}', plant_date).group()
        item['plant_date'] = plant_date

        yield item
