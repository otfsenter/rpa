# coding: utf-8

from rpa.base import LibraryComponent, keyword


class FileKeywords(LibraryComponent):

    @keyword
    def read_file(self, path_file):
        content_list = []
        with open(path_file, encoding='utf-8') as f:
            for i in f:
                row = i.strip()
                content_list.append(row)
        return content_list
