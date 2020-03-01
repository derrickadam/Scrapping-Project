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
CONCURRENT_REQUESTS_PER_DOMAIN = 32
CONCURRENT_REQUESTS_PER_IP = 32

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
    'type': 'service_account',
    'project_id': 'trudence',
    'private_key_id': '9f7ca0cf6a329e8cb3a31dc5157cb6eca366083a',
    'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDUFvbDhlUWrDHB\nm9nvDVlZPw5IRihuLlp6Y/8nrzISM/LZkUh/hPuwmJl/yc0yV6c7Ux2xp/W62Li/\neLL+ZygfGJfRiUSgHCUP+XABH7y9HLqDCPMII1O7batcxBeNhZyWTA9KtEaDsIlg\nbxq8ScgP6GZbvYHCfWzMW+cxKBsr2hAtCTgWNPiWzGiVeA4iZ9W2nZMxKFG0bhNq\nm1rUmmoL5exNvJTf4//Ug2zn0y7r0UJUW+ybMi5ueJAI4lHSjRAvICIyoArZmml5\n2TmdqEArugXc6bKzrABSAXyfobt8NYAejq7d0qFNv5+38bqwSqV+j8KlyUMA5w/3\nLEQsLSdLAgMBAAECggEAItgO/HqCWjI6DnPbbyHDTx1D7G3SUJ++76KkFdH7qO/t\n8v6iaYjgjNfVSCBQXPf3mpCCLWDJx0O5voNG7PLnrYwtzRf/NUrKcABr/VNIf81L\neyGqQ+kB5aYT5C63K+IKosqmLIDHoPUM7NH0E4EPpEVrI6FTwy82A7EJn5LWO/LP\nrwHHRzmjMNpey8YJQJfN84JHUPdNWOOpJTZH+pWE4Koh+ptrOEUyOvOXiLLGk3oT\numRlJe+JFCcn3c236DKJESfgeGKuwD4+/pAKC6u7wwR0fsDktikURzRUhTKFFNfq\navLfLjub00ZNBPvmnDZ9OZc2YaZ5W8cgzKghJIZf8QKBgQD7/qRfXLecftwCn9yE\nIlUH34ZGS72v7gLkgBhwB7oMURi4UFUnhrfMPRokjwQ02fRuSF8XrEAEIVvbe0ZT\ngoZeKWmNPnZEVs2/h3NMrD9yR7vo6fvfXFGEiKBGmmQ/jL/Rvr+vWFx0dcMoSI49\nsSZFcoVYIpDB7Rnld//6ruAtcwKBgQDXdfMkKrb1v5i4LLONdOi7Er2MffmFNxIj\n1tyrG02DLE9EqcwBVvmwS39iEObFO5MXzFvyt6A7SPIY/EY9LeWFZsUF4pzTcnEA\nF9hYwHuf9eozOPDt39WuozRHvr4JRvTtDUw5oNVNkA9KWS7zwb/Kcb7bAHRHGse1\nHjb3qNKoyQKBgCymJcGvz+iuoZTldlEDNEW82THDYcy2Q1TxTWMsO07LX7Hoqe3i\n9NX/TY6EuJ4UsDaKJC8xmfYhYwE0inVpfx1YARfBpXreVn5FJazEKEm7ZBQUwUgG\nN3tgKeXYnUKVUbd8MMKEyXzpELcmg+1yYfGUJQREu5lgxWHfLT/hlF75AoGAEbeM\nN8QfaVPI7hQW66HaZU+kMIJHW1Hs9u97E8LZ+9hP6FiCAvYw7/M1VU4Ie91rOgC+\n6tV4oodcCPvtlqhIgFC0EMjSlnyJmDVdv+aMA9pH2NBs11KZkpOu/9tKax7fkwKN\n6wsznv4ik72Do92htLbnt8Bwz0v/cgA7CuBh+ikCgYBb8PAzC5RREqEJyRO6SIpz\nF9zcF7C10rMHHekGdHb3nUjztowl0T/0DVt6SwBOy3pAWXM4kmZ6FntZk3IJHXlc\nGqqCKSRXyLgwcH5cSFplPZ1GDNlCrehtwRltTOYM1ZN44TT844dZzEkxZn9Ek6+Z\nGpnAH/RmmKoerbp274bDqg==\n-----END PRIVATE KEY-----\n',
    'client_email': 'robot-801@trudence.iam.gserviceaccount.com',
    'client_id': '117093594887116412126',
    'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
    'client_x509_cert_url': 'https://www.googleapis.com/robot/v1/metadata/x509/robot-801%40trudence.iam.gserviceaccount.com'
}
FILE_NAME = "Websites scoring"
SHEET_NAME = "New_Backend"
