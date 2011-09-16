# Scrapy settings for mangareader project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mangareader'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['mangareader.spiders']
NEWSPIDER_MODULE = 'mangareader.spiders'
DEFAULT_ITEM_CLASS = 'mangareader.items.MangareaderItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

