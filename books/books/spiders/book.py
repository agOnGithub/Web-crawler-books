import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["abc.nl"]
    start_urls = ["https://abc.nl/books"]

    def parse(self, response):
        for book in response.css('div.page-links'):
            item = BooksItem()
            item["url"] = book.css('a::attr(href)').get()
            item["title"] = book.css('a::text').get()
            yield item

        next_page = response.css('div.isotope-filterbar.callout.secondary.slider > a::attr(href)').get()
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)