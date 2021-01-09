import logging
import time
import os
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount=3, fmt='[%(asctime)s][%(levelname)s]%(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()
        sh.setFormatter(format_str)
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)


timeArray = time.localtime(time.time())
timeStr = time.strftime("%Y-%m-%d", timeArray)
if not os.path.exists('logs'):
    os.mkdir('logs')
if os.path.exists('logs/{}.txt'.format(timeStr)):
    i = 0
    TimeS = timeStr
    while os.path.exists('logs/{}.txt'.format(TimeS)):
        i += 1
        TimeS = timeStr + '-{}'.format(str(i))
    log = Logger('logs/{}.txt'.format(TimeS), level='info')
else:
    log = Logger('logs/{}.txt'.format(timeStr), level='info')


def info(text):
    log.logger.info(text)


def warm(text):
    log.logger.warning(text)


def error(text):
    log.logger.error(text)
