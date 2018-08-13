from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from master1886.util.redisutil import UtilRedis
import logging


class HuangYeSpider(CrawlSpider):
    name = 'master1886'
    start_urls = ['https://www.b2b168.com/']

    rules = [
        Rule(LinkExtractor(allow=('//info\.b2b168\.com/s168-\d+\.html',)),
             callback='parse_item', follow=True)
        ]

    def parse_item(self, response):
        conn = UtilRedis().conn
        if conn.sismember('completeurl:', response.url) or conn.sismember('indexExcepturls:', response.url):
            logging.debug(msg='该url:' + response.url + '已经爬取过了！')
            return None
        else:
            logging.info(msg='成功获取未爬取所得的url: ' + response.url)
            return conn.lpush('detailurl:', response.url)
