from ftplib import FTP
import json

from utils import config
from utils import log
from utils import Bat

import os

up = config.ReadConfig()


def check():
    log.info("检查更新")
    ftp = FTP()
    ftp.connect(up["address"], up["port"], 30)
    ftp.login(up["updata"]["username"], up["updata"]["password"])
    if not os.path.exists("pack.json"):
        ftp.retrbinary("RETR {}".format("pack.json"), open("updata/pack.json", 'wb').write, 1024)
        log.info("正在下载更新")
        download()
    else:
        if ftp.size("pack.json") != os.path.getsize("pack.json"):
            ftp.retrbinary("RETR {}".format("pack.json"), open("updata/pack.json", 'wb').write, 1024)
            log.info("正在下载更新")
            download()


def download():
    ftp = FTP()
    ftp.connect(up["address"], up["port"], 30)
    ftp.login(up["updata"]["username"], up["updata"]["password"])
    with open('updata/pack.json', 'r', encoding='UTF-8') as f:
        pack = json.load(f)
    for i in pack["files"]:
        ftp.retrbinary("RETR {}".format(i), open("updata/" + i, 'wb').write, 1024)
    install()


def CMD():
    Bat.updata()
    Bat.start()


def install():
    CMD()
    os.system('updata.bat')
