# coding: utf-8

from rpa.base import LibraryComponent, keyword


class FileKeywords(LibraryComponent):

    @keyword
    def read_file(self, path_file):
        content_list = []
        with open(path_file, encoding='utf-8') as f:
            for i in f:
                raw = i.strip()
                new_data = str(raw) + 'wuweiji'
                content_list.append(new_data)
        return content_list
