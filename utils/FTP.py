import os
import socket
import time
from ftplib import FTP

from utils import config
from utils import win10
from utils import log

ftp = FTP()
ftp.encoding = 'GB18030'
Cilent_Path = 'FTP/'
if not os.path.exists(Cilent_Path):
    log.info('不存在文件夹{0}，将创建{0}'.format(Cilent_Path))
    os.mkdir(Cilent_Path)


def Connect():
    Start_time = time.time()
    Users = config.ReadConfig()
    for i in Users["array"]:
        timeout = 30
        port = Users["port"]
        Address = Users["address"]
        try:
            ftp.connect(Address, port, timeout)
        except Exception as e:
            log.error(e)
            return
        else:
            log.info('服务器连接成功')

        try:
            ftp.login(i["username"], i["password"])
        except Exception as e:
            log.error('登录失败')
            log.error(e)
            return
        else:
            log.info('{} 登录成功'.format(i["username"]))

            Download(ftp.pwd(), i["username"])

        ftp.close()
        log.info('连接关闭')
    log.info('同步完成，用时{}秒'.format(int(time.time() - Start_time)))
    win10.Title('同步完成\n用时{}秒'.format(int(time.time() - Start_time)))


def Download(Server_Path, name):
    try:
        ftp.cwd(Server_Path)
    except Exception as e:
        log.error(e)
        win10.Title(str(e) + '\n请确认文件夹开头结尾是否是空格和是否有两个连续空格')
        return
    # print(ftp.pwd())
    Server_Dir = []
    try:
        Server_List = ftp.nlst()
    except:
        Server_List = []
    ftp.dir('.', Server_Dir.append)
    Server_Dir_2 = []
    for i in range(len(Server_Dir)):
        Server_Dir_2.append([j for j in Server_Dir[i].split(' ') if j != ''])
        if Server_Dir_2[i][0] == 'drw-rw-rw-':
            Next = ''
            for j in range(8, len(Server_Dir_2[i])):
                Next += Server_Dir_2[i][j] + ' '
            if not Next.rstrip(' ') in ['.', '..']:
                Download(Next, name)
                ftp.cwd('..')

    # print(Server_Dir_2)

    for Num in range(len(Server_List)):
        Path = '{}{}{}'.format(Cilent_Path, name, ftp.pwd() + '/')
        if not os.path.exists(Path):
            log.info('正在创建文件夹:' + Path)
            os.makedirs(Path)
        if not os.path.exists(Path + Server_List[Num]):
            log.info('正在下载“{}”'.format(Path + Server_List[Num]))
            ftp.retrbinary("RETR {}".format(Server_List[Num]), open(Path + Server_List[Num], 'wb').write, 1024)
        else:
            if ftp.size(Server_List[Num]) != os.path.getsize(Path + Server_List[Num]):
                log.info('正在下载“{}”'.format(Path + Server_List[Num]))
                ftp.retrbinary("RETR {}".format(Server_List[Num]), open(Path + Server_List[Num], 'wb').write, 1024)
