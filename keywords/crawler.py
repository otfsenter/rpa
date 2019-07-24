# coding: utf-8

import requests
from ToolLibrary.base import LibraryComponent, keyword
from bs4 import BeautifulSoup


class CrawlerKeywords(LibraryComponent):

    @keyword(name='Get Hot Spots From Baidu')
    def get_hot_from_baidu(self):
        url_hot = 'http://top.baidu.com/buzz.php?p=top10'

        response = requests.get(url=url_hot).content.decode('gbk')

        soup = BeautifulSoup(response, 'html.parser')

        tag_table = soup.find('table', {'class': 'list-table'})

        tag_tr = tag_table.find_all('td', {'class': 'keyword'})

        result = []
        for i in tag_tr:
            text_list = i.get_text().strip().split('\n')
            for text in text_list:
                if 'search' not in text:
                    result.append(text)

        return result
