# coding: utf-8

from rpa.base import LibraryComponent, keyword


class FileKeywords(LibraryComponent):

    @keyword
    def read_file(self, path_file):
        content_list = []
        with open(path_file, encoding='utf-8') as f:
            for i in f:
                content_list.append(i.strip())
        return content_list
