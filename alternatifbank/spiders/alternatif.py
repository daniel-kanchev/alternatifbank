import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from alternatifbank.items import Article


class AlternatifSpider(scrapy.Spider):
    name = 'alternatif'
    allowed_domains = ['alternatifbank.com.tr']
    start_urls = ['https://www.alternatifbank.com.tr/hakkimizda/basin-odasi/basin-bultenleri-ve-duyurular']

    def parse(self, response):
        links = response.xpath('//div[@class="item"]//a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

        next_page = response.xpath('//a[@class="next "]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h2/text()').get()
        date = response.xpath("//div[@class='date']/text()").get()
        content = response.xpath('//div[@class="outer"]/div[@class="content"]//text()').getall()
        content = " ".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
