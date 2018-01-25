# coding = utf-8
from scrapy.spider import Spider

class QuibaiSpider(Spider):
    name = "qiubai"
    allowed_domains = [
        'www.qiushibaike.com'
    ]

    start_urls = "https://www.qiushibaike.com/8hr/page/1/"

    def parse(self, response):
