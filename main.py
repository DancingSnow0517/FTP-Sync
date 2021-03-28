from utils import log
from utils import command
from utils import AutoTime
from utils import win10
from utils import updata
if __name__ == '__main__':
    # ico.img()
    command.command_start()
    AutoTime.Auto()
    win10.Title('程序已启动\n同步已开启')
    log.info('程序已启动，输入help查看帮助')
    updata.check()

