import scrapy

class RawHtmlItem(scrapy.Item):
    url = scrapy.Field()
    fetch_ts = scrapy.Field()
    status = scrapy.Field()
    content_type = scrapy.Field()
    sha256 = scrapy.Field()
    html = scrapy.Field()
