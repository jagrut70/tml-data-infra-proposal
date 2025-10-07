# Polite Crawler Skeleton

- Scrapy-based with Playwright option for JS rendering.
- robots.txt compliance, per-domain rate limiting, adaptive backoff.
- Early dedup via SHA256/simhash/phash to avoid duplicate fetches.
- Emits records to Kafka topics (`raw_html`, `media`).

> For public sharing, no API keys or secrets are included.
