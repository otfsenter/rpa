# coding: utf-8
import importlib

import robot
from pyrpa.base import DynamicCore
from pyrpa.utils import LibraryListener
from pyrpa.class_data import MODULE_CLASS_DICT, MODULE, KEYWORDS

__version__ = '0.0.1'


class pyrpa(DynamicCore):
    """
    ToolLibrary is a tool library for company.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        self._running_on_failure_keyword = False

        class_list = []
        for file_name in MODULE_CLASS_DICT.keys():
            module_keywords_file_name_str = '.'.join([MODULE, KEYWORDS, str(file_name)])

            cls = getattr(
                importlib.import_module(module_keywords_file_name_str),
                MODULE_CLASS_DICT.get(file_name)
            )
            class_list.append(cls(self))

        libraries = class_list

        DynamicCore.__init__(self, libraries)
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()

    def run_keyword(self, name, args, kwargs):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            raise Exception('no keyword')
