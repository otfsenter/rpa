# coding: utf-8

from .librarylistener import LibraryListener
from .toolversion import TOOL_VERSION
from .types import is_noney, is_falsy


def escape_xpath_value(value):
    if '"' in value and '\'' in value:
        parts_wo_apos = value.split('\'')
        return "concat('%s')" % "', \"'\", '".join(parts_wo_apos)
    if '\'' in value:
        return "\"%s\"" % value
    return "'%s'" % value
