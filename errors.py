# coding: utf-8


class ToolLibraryException(Exception):
    ROBOT_SUPPRESS_NAME = True


class ElementNotFound(ToolLibraryException):
    pass


class WindowNotFound(ToolLibraryException):
    pass


class CookieNotFound(ToolLibraryException):
    pass


class NoOpenBrowser(ToolLibraryException):
    pass
