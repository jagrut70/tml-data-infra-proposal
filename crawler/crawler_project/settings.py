BOT_NAME = "crawler_project"
SPIDER_MODULES = ["crawler_project.spiders"]
NEWSPIDER_MODULE = "crawler_project.spiders"
ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS_PER_DOMAIN = 4
DOWNLOAD_DELAY = 0.5
ITEM_PIPELINES = {
    "crawler_project.pipelines.HashAndStampPipeline": 300,
}
