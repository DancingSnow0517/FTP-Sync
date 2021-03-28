import json
import os

from utils import log


class Info:
    VERSION = 'V1.1'
    updata = {
        "username": "1",
        "password": "1"
    }


def ReadConfig():
    with open('config.json', 'r', encoding='UTF-8') as f:
        return json.load(f)


def WriteConfig(c):
    with open('config.json', 'w', encoding='UTF-8')as f:
        json.dump(c, f, indent=4)


if not os.path.exists('config.json'):
    js = {"array": [], "address": '0.0.0.0', "port": 21, "Sync": ["14:40"], "updata": Info.updata,
          "version": Info.VERSION}
    WriteConfig(js)
    log.info('未找到配置文件，现已生成')
