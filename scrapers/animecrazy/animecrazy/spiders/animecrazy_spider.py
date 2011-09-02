from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from animecrazy.items import AnimecrazyItem

class AnimeCrazySpider(BaseSpider):

    name = 'animecrazy.net'
    base_url = 'http://'+name
    
    allowed_domains = ['animecrazy.net']

    start_urls = [
        "http://www.animecrazy.net/anime-index/"
    ]

    def clean_type(self, text):
        text = text.replace('(', '')
        text = text.replace(')', '')
        return text.strip()


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        animes = hxs.select("//ul[@class='truindexlist']/li")
        items = []
        for anime in animes:
            item = AnimecrazyItem()
            item['title'] = anime.select('a/text()').extract()[0]
            item['link'] = self.base_url + anime.select('a/@href').extract()[0]
            item['type'] = self.clean_type(anime.select('text()').extract()[0])
            items.append(item)

        for item in items:
            request = Request(item['link'], callback=self.parse_detail)
            request.meta['item'] = item
            yield request

    def parse_detail(self, response):

        hxs = HtmlXPathSelector(response)
        
        item = response.request.meta['item']

        item['description'] = hxs.select('//p[@class="desc"]/text()').extract()[-1]      
        item['genres'] = hxs.select('//span[@id="genre"]/span/a[@class="tag"]/text()').extract()[:-1] 
        item['year'] =  hxs.select('//div[@class="epCount"]/p/text()')[-1].extract().strip()

        return item

