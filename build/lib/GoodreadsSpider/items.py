# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class GoodreadsspiderItem(Item):
    # define the fields for your item here like:
    book_name = Field()
    author = Field()
    avg_rating = Field()
    rating_count = Field()
    review_count = Field()
    genre = Field()
    book_format = Field()
    page_count = Field()
