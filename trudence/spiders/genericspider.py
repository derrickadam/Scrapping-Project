# -*- coding: utf-8 -*-
import json
import urllib

import gspread
import scrapy
from oauth2client.service_account import ServiceAccountCredentials
from scrapy import Request

from trudence.items import TrudenceItem
from trudence.settings import SHEET_NAME, FILE_NAME, CREDENTIALS


class GenericSpider(scrapy.Spider):
    name = 'genericspider'
    headers = {
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    custom_settings = {
        # 'HTTPCACHE_ENABLED': "True"
    }
    ignore_words = ["mailto", ".pdf", ".xlsx", ".csv", 'tel:', '.jpg', '.png']

    def start_requests(self):
        self.get_google_sheet_data()
        for url in self.domains[:10]:
            yield Request(url, self.parse_main_page, headers=self.headers, meta={"domain": url})

    def parse_main_page(self, response):
        meta = {"domain": response.meta['domain']}
        for url in set(response.css("a::attr(href)").getall()):
            if self.check_if_ignore(url):
                continue
            parsed_uri = urllib.parse.urlparse(response.url)
            domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
            if 'http' in url and domain not in url:
                continue
            yield response.follow(url, self.extract_content, meta=meta)
        yield from self.extract_content(response)

    def extract_content(self, response):
        item = TrudenceItem()
        try:
            item["content"] = " ".join([i.strip() for i in
                                        response.xpath("//*[not(self::script) and not(self::style)]/text()").getall() if
                                        i.strip() != ""])
            item["url"] = response.url
            item["domain"] = response.meta["domain"]
            yield item
        except Exception as e:
            # Exception may happen when following a link .pdf or @email ...
            print(e)

    def get_google_sheet_data(self, proxy=False):
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        with open("cred.json", "w+") as file:
            file.write(json.dumps(CREDENTIALS))

        creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
        gc = gspread.authorize(creds)
        # Open a worksheet from spreadsheet with one shot
        self.wks = gc.open(FILE_NAME).worksheet(SHEET_NAME)
        self.domains = self.wks.col_values(1)[1:]
        self.domains = [correct_domain(url) for url in self.domains]
        self.keywords = self.wks.row_values(1)[4:]

    def check_if_ignore(self, url):
        for i in self.ignore_words:
            if i in url:
                return True
        return False



def correct_domain(url):
    if 'http' not in url:
        return "http://" + url
    return url
