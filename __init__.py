# coding: utf-8
from ToolLibrary.base import DynamicCore
from ToolLibrary.keywords import (
    CrawlerKeywords,
    FileKeywords,
    DataKeywords
)
from ToolLibrary.utils import LibraryListener

__version__ = '0.0.1'


class ToolLibrary(DynamicCore):
    """
    ToolLibrary is a tool library for company.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):
        self._running_on_failure_keyword = False
        libraries = [
            CrawlerKeywords(self),
            FileKeywords(self),
            DataKeywords(self),
        ]
        DynamicCore.__init__(self, libraries)
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()

    def run_keyword(self, name, args, kwargs):
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            self.failure_occurred()
            raise
