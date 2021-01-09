from threading import Thread
from utils import FTP
from utils import config
from utils import AutoTime
from utils import log
from utils import Bat

Help_msg = '''“ftp”同步ftp服务器文件到本地
“stop”关闭软件
“help”获取帮助
“add <用户名> <密码>”添加一个账户
“remove <用户名>”删除一个账号
“list”显示已经添加的账户
”bat“生成 启动/退出 脚本'''

Flag = True


class Command(Thread):
    def __init__(self):
        super().__init__()
        self.shutdown_flag = True

    def run(self):
        while Flag:
            Cmd = input('')
            if Cmd == 'stop':
                command_stop()
                log.warm('正在关闭，清稍后')
                continue
            if Cmd == 'ftp':
                try:
                    FTP.Connect()
                except Exception as e:
                    log.error(e)
                continue
            if Cmd in ['help', '?']:
                print(Help_msg)
                continue
            if 'add' in Cmd and len(Cmd.split(' ')) == 3:
                username = Cmd.split(' ')[1]
                password = Cmd.split(' ')[2]
                js = config.ReadConfig()
                js["array"].append({"username": username, "password": password})
                config.WriteConfig(js)
                log.info('已成功添加用户：' + username)
                continue
            if Cmd == 'list':
                js = config.ReadConfig()
                UserList = ''
                for i in js["array"]:
                    UserList += i["username"] + ','
                print(UserList.rstrip(','))
                print('共{}名用户'.format(len(js["array"])))
                continue
            if 'remove' in Cmd and len(Cmd.split(' ')) == 2:
                js = config.ReadConfig()
                for i in js["array"]:
                    if i["username"] == Cmd.split(' ')[1]:
                        js["array"].remove(i)
                config.WriteConfig(js)
                log.info('已将用户{}移除'.format(Cmd.split(' ')[1]))
                continue
            if Cmd == 'bat':
                Bat.start()
                Bat.kill()
                log.info('已生成run.vbs启动脚本')
                log.info('已生成kill.bat退出脚本')
                continue

            log.error('未知命令，请输入help查看帮助')


def command_start():
    CM = Command()
    CM.start()


def command_stop():
    global Flag
    Flag = False
    AutoTime.AutoStop()
