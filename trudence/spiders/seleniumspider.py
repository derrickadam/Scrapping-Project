# -*- coding: utf-8 -*-

from trudence.spiders.proxyspider import ProxySpider


class SeleniumspiderSpider(ProxySpider):
    name = 'seleniumspider'
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'trudence.middlewares.SeleniumMiddleware': 10,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': 100,
            'trudence.middlewares.CustomProxyMiddleware': 350,
            'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
        },
        "CONCURRENT_REQUESTS": 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'CONCURRENT_REQUESTS_PER_IP': 1
    }
    run_next_enabled = False
    bad_texts = ["The requested URL could not be retrieved", "The service is unavailable", "Access Denied"]

    def __init__(self, is_master=True, lower_bound=0, use_proxy=False, **kwargs):
        super().__init__(is_master=True, lower_bound=0, **kwargs)
        self.use_proxy = (use_proxy is not False)
