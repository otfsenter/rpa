# coding: utf-8
import robot
from rpa.base import DynamicCore
from rpa.keywords import (
    CrawlerKeywords,
    FileKeywords
)
from rpa.utils import LibraryListener

__version__ = '0.0.1'


class rpa(DynamicCore):
    """
    ToolLibrary is a tool library for company.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        self._running_on_failure_keyword = False
        libraries = [
            CrawlerKeywords(self),
            FileKeywords(self)
        ]
        DynamicCore.__init__(self, libraries)
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()

    def run_keyword(self, name, args, kwargs):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            raise Exception('no keyword')
