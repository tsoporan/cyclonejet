# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class AnimecrazyItem(Item):
    title = Field()
    type = Field() #anime,movie,ova etc.
    link = Field()
    description = Field()
    genres = Field()
    year = Field()

