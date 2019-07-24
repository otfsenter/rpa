# coding: utf-8

from ToolLibrary.base import LibraryComponent, keyword


class DataKeywords(LibraryComponent):

    @keyword
    def organization_messages(self, name_index, msg_index_range, data_list):
        name_index = int(name_index)

        new_list = []
        for row_index, row_list in enumerate(data_list):
            name = row_list[name_index - 1]

            start_index = int(str(msg_index_range).split('-')[0])
            end_index = int(str(msg_index_range).split('-')[1])
            msg_list = row_list[start_index - 1: end_index]
            msg = ' '.join([str(i) for i in msg_list])
            new_list.append([name, msg])
        return new_list