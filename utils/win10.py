from win10toast import ToastNotifier
import time

to = ToastNotifier()


def Title(text):
    try:
        to.show_toast('FTP-Sync', text, duration=3, icon_path='py.ico')
    except:
        time.sleep(5)
        to.show_toast('FTP-Sync', text, duration=3, icon_path='py.ico')
