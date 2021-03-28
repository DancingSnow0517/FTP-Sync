import wx
import wx.adv

from utils import FTP
from utils import command


class BarIcon(wx.adv.TaskBarIcon):
    ICON = "py.ico"
    ID_SYNC = wx.NewId()
    ID_EXIT = wx.NewId()
    TITLE = "FTP-Sync"

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)
        self.Bind(wx.EVT_MENU, self.OnSync, id=self.ID_SYNC)
        self.Bind(wx.EVT_MENU, self.OnExit, id=self.ID_EXIT)

    def OnSync(self, event):
        wx.MessageBox('开始同步', 'FTP-Sync')

    def OnExit(self, event):
        wx.Exit()
        command.command_stop()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])

    def getMenuAttrs(self):
        return [('开始同步', self.ID_SYNC),
                ('退出', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        BarIcon()


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True


def Show():
    app = MyApp()
    app.MainLoop()
