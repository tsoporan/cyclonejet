# Scrapy settings for animecrazy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'animecrazy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['animecrazy.spiders']
NEWSPIDER_MODULE = 'animecrazy.spiders'
DEFAULT_ITEM_CLASS = 'animecrazy.items.AnimecrazyItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

