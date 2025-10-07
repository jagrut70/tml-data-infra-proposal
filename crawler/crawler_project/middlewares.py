from scrapy.downloadermiddlewares.retry import RetryMiddleware

class PoliteRetryMiddleware(RetryMiddleware):
    # Customize retry/backoff if needed
    pass
