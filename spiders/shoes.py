import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Shoes(CrawlSpider):
    name='shoes'

    allowed_domains=["adidas.com"]

    url_list=["https://www.adidas.com/us/shoes?start={}".format(i) for i in range (0,2640)]
    start_urls=url_list

    rules = (
            Rule(LinkExtractor(restrict_xpaths='//a[contains(@class,"product-link")]',
                deny=('_[WM]\.html',)),
                callback='parse'),
            # Rule to follow arrow to next product grid
            Rule(LinkExtractor(restrict_xpaths='//li[@class="pagging-arrow right-arrow"]'),
                follow=True),
        )

    def parse(self, response):
        for elem in response.xpath('//div[@class="gl-product-card__media"]//img'):
            img_url = elem.xpath("@src").extract_first()
    
            yield {'image_urls': [img_url]}  
