# coding: utf-8

from collections import namedtuple

ToolVersion = namedtuple('ToolVersion', 'major minor micro')
TOOL_VERSION = ToolVersion(major=0, minor=0, micro=1)
