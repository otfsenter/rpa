# coding: utf-8
from robot.utils import is_string

try:
    from robot.utils import PY3
except ImportError:
    import sys

    PY3 = sys.version_info[0] == 3


def is_truthy(item):
    if is_string(item):
        return item.upper() not in ('FALSE', 'NO', '', 'NONE')
    return bool(item)


def is_falsy(item):
    return not is_truthy(item)


def is_noney(item):
    return item is None or is_string(item) and item.upper() == 'NONE'
