import scrapy
from mySpider.items import SmzdmItem


class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/']

    def parse(self, response):
        li_list = response.xpath("//ul[@class='feed-list-hits']/li")
        for li in li_list:
            item = SmzdmItem()
            item['title'] = li.xpath(".//div[@class='z-feed-content ']/h5/a/text()").extract_first()
            item['price'] = li.xpath(".//div[@class='z-highlight']/a/text()").extract_first().strip()
            item['detail_url'] = li.xpath(".//div[@class='z-feed-content ']/h5/a/@href").extract_first()
            yield scrapy.Request(
                item['detail_url'],
                callback=self.parse_comment,
                meta={'item': item},
                dont_filter=False
            )

    def parse_comment(self, response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@id='commentTabBlockNew']/ul[@class='comment_listBox']/li")
        for li in li_list:
            comment = li.xpath(
                ".//div[@class='comment_conBox']/div[@class='comment_conWrap']/div[@class='comment_con']/p/span/text()"
            ).extract()
            item['comment'] = ''.join(comment).strip()
            item['comment_date'] = li.xpath(
                ".//div[@class='comment_conBox']/div[@class='comment_avatar_time ']/div[@class='time']/meta/@content"
            ).extract()
            yield item
        next_url = response.xpath(
            "//div[@id='commentTabBlockNew']/ul[@class='pagination']/li[@class='pagedown']/a/@href"
        ).extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse_comment,
                meta={"item": item},
                dont_filter=False
            )