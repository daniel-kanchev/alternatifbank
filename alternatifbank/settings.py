BOT_NAME = 'alternatifbank'
SPIDER_MODULES = ['alternatifbank.spiders']
NEWSPIDER_MODULE = 'alternatifbank.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'alternatifbank.pipelines.DatabasePipeline': 300,
}
