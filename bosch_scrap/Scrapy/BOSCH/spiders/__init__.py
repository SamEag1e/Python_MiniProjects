"""Scrape BOSCH.

Hello
"""

import scrapy


class Bosch(scrapy.Spider):
    name = "items"
    start_urls = [
        "https://www.bosch-repair-service.com/en/productsearch/NaN-NaN?product_search=026",
    ]

    def parse(self, response):
        yield {
            "h4": response.css("div.col-md-5 h4.violet-blue-gradient-text a").get(),
        }

        next_page = response.css('li a.showwait::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
