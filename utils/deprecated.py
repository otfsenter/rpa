# coding: utf-8

import warnings


class Deprecated(object):

    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def __get__(self, instance, owner):
        self._warn()
        return getattr(instance, self.new_name)

    def __set__(self, instance, value):
        self._warn()
        setattr(instance, self.new_name, value)

    def _warn(self):
        warnings.warn('"SeleniumLibrary.%s" is deprecated, use '
                      '"SeleniumLibrary.%s" instead.'
                      % (self.old_name, self.new_name),
                      DeprecationWarning)
