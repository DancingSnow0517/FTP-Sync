from os.path import dirname, abspath

CMDS = "taskkill /F /IM main.exe /T \n" \
       "move updata\*.* .\ \n" \
       "run.vbs\n" \
       "del updata.bat"

PATH = abspath('./')


def kill():
    with open('kill.bat', 'w') as f:
        f.write('taskkill /F /IM main.exe /T')


def start():
    with open('run.vbs', 'w') as f:
        f.write(f'set wscriptObj = CreateObject("Wscript.Shell")\nwscriptObj.run "{PATH}\\main.exe",0')


def updata():
    with open('updata.bat', 'w') as f:
        f.write(CMDS)
