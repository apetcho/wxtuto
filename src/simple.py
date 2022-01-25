#!/usr/bin/env python3
import wx

USE_WIT = False
AppBaseClass = wx.App
if USE_WIT:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp


class MxFrame(wx.Frame):
    """This is MyFrame."""

    def __init__(self, parent, title):
        pass

    def OnTimeToClose(self, event):
        pass

    def OnFunButton(self, event):
        pass


class MyApp(AppBaseClass):
    def OnInit(self):
        pass


def main():
    app = MyApp(redirect=True)
    app.MainLoop()


if __name__ == "__main__":
    main()
