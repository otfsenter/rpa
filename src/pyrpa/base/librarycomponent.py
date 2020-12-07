# coding: utf-8
import os

from pyrpa.utils import is_noney
from .context import ContextAware
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from .robotlibcore import PY2


class LibraryComponent(ContextAware):

    def info(self, msg, html=False):
        logger.info(msg, html)

    def debug(self, msg, html=False):
        logger.debug(msg, html)

    def log(self, msg, level='INFO', html=False):
        if not is_noney(level):
            logger.write(msg, level.upper(), html)

    def warn(self, msg, html=False):
        logger.warn(msg, html)

    @property
    def log_dir(self):
        try:
            logfile = BuiltIn().get_variable_value('${LOG FILE}')
            if logfile == 'NONE':
                return BuiltIn().get_variable_value('${OUTPUTDIR}')
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwdu() if PY2 else os.getcwd()
