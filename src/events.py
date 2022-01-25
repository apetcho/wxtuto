#!/usr/bin/env python3
import wx
from six import print_

print_(wx.version())


class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        pass

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
