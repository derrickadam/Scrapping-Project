# -*- coding: utf-8 -*-

# Scrapy settings for trudence project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'trudence'

SPIDER_MODULES = ['trudence.spiders']
NEWSPIDER_MODULE = 'trudence.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'trudence (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'trudence.middlewares.TrudenceSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'trudence.middlewares.TrudenceDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'trudence.pipelines.TrudencePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

CREDENTIALS = {
  "type": "service_account",
  "project_id": "scraping-project-268618",
  "private_key_id": "d72e89deaf8efbc806e371e994cfe0036573795b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9EbykzBPEaazV\n92ka3CDCMTVnhzBI1kDG/gHEPDGq8mBV4z/t1l+7v1L0J5vKZzireneuV3iCk7aj\npLDOvdlJa1QIfOKPKhzSuiuLDPaBJP1j128SPqqGyuA3AKiMLMLuX4ldQLRDRQee\n3bIhV4zes4tgIk5tyjp13NDWapCndu4aanIGUVcQ3703cQPlsaKeYKvWYGYPRmFN\n/+TdFLNXm9Y968K3m98n/5cOMe3ZZlSkP9+QQrpWibym9s0seUruecgRbim2cnyW\nHZVP9TR3MlfOhJrSf2/bFrf61y+ndpGlla4QAYYef73LHUm7AFHICqnIKgzh1oFw\n7rnx8aLvAgMBAAECggEABRp6dhRQIEgd8zSXcLMqazN61o2OnxixbO2kTJC3Yn7i\nXM8ihZ/4u4+hhJehG+iHXhGTM3CG/zdPgcFLSHlVaSbtgMEmOGkRmBqQXFOAP+Io\nuM4y4FIytiq5vKJW6lm29Uo84fiCJSKy3vXq/f1n/wbnpzOl3E7OHypTtMXxm6ON\nS7hINVa175sIQwL4nAvoDUu10XXj0OSgMt/sWggVykneAPK8eaCn8Onwza/peyuF\nBU67DBDlKHXqpcrlEcYPZDohVugN9J3QBtxh/c0ORd0z5xPVTj37Cj3dmVfn9neN\no9ltSkRXCR6qLVaNRsnPnYobhdm8bFF1js/BVfUNCQKBgQDm3y8hdR+53R39Yoor\nq0PO5ouNEp/GvQQMUpoRVtp8uCctv/FyfBrzHQcxFPpAEDP/LoTRgb4FoY0patBh\nRKzngyLaf7My1r4b4m8/Aiza8/x+pXZ+Etclo+Ll2XfoASzuAiChWVtJW9Q+4QtR\nunhX5Syad7fOgCwZMv+5amgQwwKBgQDRpc18nYGZ+QHgh+FBbuK9+03LrH7hxtXI\nZExS4TCLFQNy+XT4VovWiupB2UbZelO8O3JbXRtSP+baL+pijAfXlWBAoU1vd/pT\nlIITa0wshJayMQ16XjkbuugDcqDvm/AwrUnChOvNHnZXsj/mJyhC6pPP73M3knOU\nDR6XgiCCZQKBgQDkmJo3G5yFUU6PhJFg+dxTMe19irJPevpWJTfN8Vy23zRT1VkB\nzaZ1kAl97NJ4ulJx2iLCux9mvfZiyxN3LCOzvCG3jXfm38AvJf6WudWmGq2ozLbN\n0GPdLi/M/I4AV6GgLNUYTbzYnydB91xY2TStewq2C9IgksKXVOrmMVjHNwKBgAgf\nP03DoGDBt+Pl/8EUNa6cjNAGN8gxdtjToe1YEhRhVQfgSDrSx4ohSaARdeA5EANr\n3itR+Rv/o8byMkdtG2SrwdXfKevWnxkb2Mo9zu6umFQA+H+0JMxBOnnfuAJwbSbF\nn+TsV2JT+su8+SLGg5XMFrvoj/MoNlgXBgdioDXNAoGBANm++G/anC26n0e3dLqi\n0TV0f/pc94QV0N8R7GIJYlS7QoeDUNvX7hI0RVx29XUPv8IE9MGA32AhmuNRHaCQ\n8EtiB/ytX2onLlBp7ZxLYIJoQbCjV5BHagw1B6+fvgoeAxREAvPJ5l94Gi9ueTah\nwGjQLNVOHhrDl6jZMcZSRvV/\n-----END PRIVATE KEY-----\n",
  "client_email": "robot-985@scraping-project-268618.iam.gserviceaccount.com",
  "client_id": "118321807277285175744",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/robot-985%40scraping-project-268618.iam.gserviceaccount.com"

}
FILE_NAME = "Scrapping Project"
SHEET_NAME = "Sheet1"
