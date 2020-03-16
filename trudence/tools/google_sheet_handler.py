import json
from itertools import zip_longest

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging

from itertools import groupby

import requests
import xlsxwriter
import datetime
from pytz import timezone


class GoogleSheetHandler:
    def __init__(self, credentials=None, sheet_name="", main_sheet="", conf_sheet=""):
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.logger = logging.getLogger(__name__)

        with open("cred.json", "w+") as file:
            file.write(json.dumps(credentials))

        credentials = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
        self.gc = gspread.authorize(credentials)

        # Open a worksheet from spreadsheet with one shot
        self.wks_main = self.gc.open(sheet_name).worksheet(main_sheet)
        self.wks_conf = self.gc.open(sheet_name).worksheet(conf_sheet)

    def get_domain(self):
        domains = self.wks_main.col_values(1)[2:]
        domains = [self.correct_domain(url) for url in domains]
        self.logger.info(f"Domains found {domains}")
        return domains

    def get_keywords(self):
        try:
            keywords = [i.lower() for i in self.wks_main.row_values(2)[4:]]
            weights = {i: int(j) for i, j in zip_longest(keywords, self.wks_main.row_values(1)[4:], fillvalue=1)}
        except Exception as e:
            logging.error(f"Error in syntax, keyword must be a string, weights must be integers {e}")
        self.logger.info(f"Keywords : {keywords}")
        self.logger.info(f"Weights  : {weights}")
        return keywords, weights

    def correct_domain(self, url):
        if 'http' not in url:
            return "http://" + url
        return url

    def get_totals(self):
        totals = self.wks_main.col_values(4)[2:]
        self.logger.info(f"Totals found {totals}")
        return totals

    def get_batches_sizes(self):
        batches = {i: int(j) for i, j in zip(self.wks_conf.col_values(1)[1:], self.wks_conf.col_values(2)[1:])}
        self.logger.info(f"Batches sizes  found : {batches}")
        return batches

    def upload_results(self, spider, counts):
        last_keyword = xlsxwriter.utility.xl_col_to_name(len(spider.keywords) + 3)
        sheet_cells = self.wks_main.range(f'B3:{last_keyword}{len(spider.all_domains) + 3}')

        updated_cells = []
        for domain, (_, cell_list) in zip(spider.all_domains, groupby(sheet_cells, lambda x: x._row)):
            if domain not in spider.domains:
                continue
            cell_list = [i for i in cell_list]
            values = []
            for keyword in spider.keywords:
                values += [counts.get(domain, {}).get(keyword, 0) * spider.weights[keyword]]
            sub_domains_counts = counts.get(domain, {}).get("sub_domains", 0)
            time = datetime.datetime.now(timezone('EST')).strftime("%Y-%m-%d %H:%M:%S")
            print(values)
            total_score = int(sum(values))
            values = [sub_domains_counts, time, total_score] + values
            for cell, value in zip(cell_list, values):
                cell.value = value
            self.logger.info(f"{domain} : {values}")
            updated_cells += cell_list
        self.wks_main.update_cells([i for i in updated_cells])
