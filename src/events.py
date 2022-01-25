#!/usr/bin/env python3
import wx
from six import print_

print_(wx.version())


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        self.Bind(wx.EVT_SIZE, self.onSize)
        wx.CallAfter(self.after, 1, 2, 3)

    def after(self, a, b, c):
        pass

    def onSize(self, event):
        pass


class MyApp(wx.App):
    def OnInit(self):
        pass

    def OnExit(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
