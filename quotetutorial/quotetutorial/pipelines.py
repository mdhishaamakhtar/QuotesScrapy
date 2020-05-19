# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            title text,
                            author text,
                            tag text)
                            """)

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values(?,?,?)""", (
            item['title'],
            item['author'],
            item['tag']
        ))
        self.conn.commit()

    def process_item(self, item, _spider):
        self.store_db(item)
        return item
