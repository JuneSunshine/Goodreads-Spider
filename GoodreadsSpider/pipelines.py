# -*- coding: utf-8 -*-
import pymysql as pq

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GoodreadsspiderPipeline(object):
    def __init__(self):
        self.conn = pq.connect(host='localhost', user='root', passwd='83252253',db='Goodreads', charset='utf8')
        self.cur = self.conn.cursor()

    # def __init__(self, dbpool):
    #     self.dbpool = dbpool

    # def from_settings(self, cls, settings):
    #     dbparams = dict(
    #         host=settings['MYSQL_HOST'],
    #         db=settings['MYSQL_DBNAME'],
    #         user=settings['MYSQL_USER'],
    #         passwd=settings['MYSQL_PASSWD'],
    #         charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
    #         cursorclass=pq.cursors.DictCursor,
    #         use_unicode=False,
    #     )
    #     dbpool = adbapi

    def process_item(self, item, spider):
        self.conn = pq.connect(host='localhost', user='root', passwd='83252253', db='Goodreads', charset='utf8')
        self.cur = self.conn.cursor()
        book_name = item.get("book_name", "N/A")
        author = item.get("author", "N/A")
        avg_rating = item.get("avg_rating", "N/A")
        rating_count = item.get("rating_count", "N/A")
        review_count = item.get("review_count", "N/A")
        genre = item.get("genre", "N/A")
        book_format = item.get("book_format", "N/A")
        page_count = item.get("page_count", "N/A")

        sql = "insert into goodreads(book_name, author, avg_rating, rating_count, review_count, genre, book_format, page_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            self.cur.execute(sql, (book_name, author, avg_rating, rating_count, review_count, genre, book_format, page_count))
            self.conn.commit()
        except Exception as error:
            print("EXCEPTION!!!", error.args[0], error.args[1])
            # conn.rollback()
        # finally:
        #     self.cur.close()
        #     self.conn.close()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

