from threading import Thread

from utils import config
from utils import FTP
from utils import log

from utils import win10
import time
import sys

TimeList = config.ReadConfig()["Sync"]

Flag = True


class Sync(Thread):
    def __init__(self):
        super().__init__()
        self.shutdown_flag = True

    def run(self):
        log.info('已开启自动同步')
        # win10.Title('已开启自动同步')
        while Flag:
            time_array = time.localtime(time.time())
            if time_array.tm_hour < 10:
                if time_array.tm_min < 10:
                    T = '0' + str(time_array.tm_hour) + ':0' + str(time_array.tm_min)
                else:
                    T = '0' + str(time_array.tm_hour) + ':' + str(time_array.tm_min)
            else:
                if time_array.tm_min < 10:
                    T = '0' + str(time_array.tm_hour) + ':' + str(time_array.tm_min)
                else:
                    T = str(time_array.tm_hour) + ':' + str(time_array.tm_min)
            if T in TimeList:
                win10.Title('开始同步')
                try:
                    FTP.Connect()
                except Exception as e:
                    log.error(e)
            if not Flag:
                break
            time.sleep(5)
            if not Flag:
                break
            time.sleep(5)
            if not Flag:
                break
            time.sleep(5)
            if not Flag:
                break
            time.sleep(5)
            if not Flag:
                break
            time.sleep(5)
            if not Flag:
                break
            time.sleep(5)


def Auto():
    AT = Sync()
    AT.start()


def AutoStop():
    global Flag
    Flag = False
