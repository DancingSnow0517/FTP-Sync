def kill():
    with open('kill.bat','w') as f:
        f.write('taskkill /F /IM main.exe /T')


def start():
    with open('run.vbs','w') as f:
        f.write('set wscriptObj = CreateObject("Wscript.Shell")\nwscriptObj.run "main.exe",0')
