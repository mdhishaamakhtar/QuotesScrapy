import scrapy
from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        item = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
            if not tag:
                tag = ['none']
            tags = ""
            for i in tag:
                tags = tags + i + ","
            tags = tags[:-1]
            item['title'] = title[0]
            item['author'] = author[0]
            item['tag'] = tags
            yield item

        next_page = response.css('li.next a').xpath("@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
