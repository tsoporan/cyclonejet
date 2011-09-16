# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class MangareaderItem(Item):
    title = Field()
    link = Field()
    description = Field()
    year = Field()
    genres = Field()
    author = Field()
