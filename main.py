# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from utils import log
from utils import command
from utils import AutoTime
from utils import win10
from utils import ico

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # ico.img()
    command.command_start()
    AutoTime.Auto()
    win10.Title('程序已启动\n同步已开启')
    log.info('程序已启动，输入help查看帮助')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
