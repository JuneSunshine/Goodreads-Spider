from scrapy.selector import Selector
from scrapy.http import Request

from scrapy.contrib.loader import ItemLoader
import scrapy
from GoodreadsSpider.items import GoodreadsspiderItem
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class goodreadsSpider(scrapy.Spider):

    name = "goodreadspider"
    allowed_domains = ["www.goodreads.com"]


    def start_requests(self):
        for i in range(12817, 15000):
            url = "https://www.goodreads.com/book/show/%s" % str(i)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        item = GoodreadsspiderItem()

        info_list = response.xpath('//div[@class="leftContainer"]')
        extra_info_list = response.xpath('//div[@class="rightContainer"]')

        for info, extra_info in zip(info_list, extra_info_list):
            try:
                item["book_name"] = info.xpath('.//h1[@id="bookTitle"]/text()').extract_first().strip()
                item["author"] = info.xpath('.//span[@itemprop="name"]/text()').extract_first()
                item["avg_rating"] = info.xpath('.//span[@itemprop="ratingValue"]/text()').extract_first()
                item["rating_count"] = info.xpath('.//span[@class="votes value-title"]/text()').extract_first().strip()
                item["review_count"] = info.xpath('.//span[@class="count value-title"]/text()').extract_first().strip()
                item["genre"] = ', '.join(extra_info.xpath('.//a[@class="actionLinkLite bookPageGenreLink"]/text()').extract())
                item["book_format"] = info.xpath('.//span[@itemprop="bookFormat"]/text()').extract_first()
                item["page_count"] = info.xpath('.//span[@itemprop="numberOfPages"]/text()').extract_first().split()[0]
                yield item
            except:
                pass


