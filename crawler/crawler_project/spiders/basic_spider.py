import scrapy
from ..items import RawHtmlItem

class BasicSpider(scrapy.Spider):
    name = "basic"
    start_urls = ["https://example.com/"]
    custom_settings = {"ROBOTSTXT_OBEY": True}

    def parse(self, response):
        yield RawHtmlItem(
            url=str(response.url),
            status=response.status,
            content_type=response.headers.get('Content-Type', b'').decode('utf-8'),
            html=response.text,
        )
