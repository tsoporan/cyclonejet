from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from mangareader.items import MangareaderItem
from scrapy import log

class MangaReaderSpider(BaseSpider):

    name = 'mangareader.net'

    base_url = 'http://' + name
    
    allowed_domains = ['mangareader.net']

    start_urls = [
        "http://www.mangareader.net/alphabetical"
    ]

    def parse(self, response):
        
        hxs = HtmlXPathSelector(response)

        mangas = hxs.select('//ul[@class="series_alpha"]/li')
    
        if mangas:
            
            items = []

            for manga in mangas:
                item = MangareaderItem()
               
                item['title'] = manga.select('a/text()')[0].extract()
                item['link'] = self.base_url + manga.select('a/@href')[0].extract()

                items.append(item)

            for item in items:
                request = Request(item['link'], callback=self.parse_detail)
                request.meta['item'] = item
                yield request


    def parse_detail(self, response):

        hxs = HtmlXPathSelector(response)

        item = response.request.meta['item']

        prop_table = hxs.select('//div[@id="mangaproperties"]/table')[0]

        item['year'] = prop_table.select('//td/text()')[6].extract() 
        item['author'] = prop_table.select('//td/text()')[10].extract()
        item['genres'] = prop_table.select('//td/a/span[@class="genretags"]/text()').extract() 

        item['description'] = hxs.select('//div[@id="readmangasum"]/p/text()').extract()

        return item
