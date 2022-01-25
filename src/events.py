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
        print_(f"Called via wx.CallAfter: {a}, {b}, {c}")

    def onSize(self, event: wx.Event):
        print_(repr(event.Size))
        event.Skip()


class MyApp(wx.App):
    def OnInit(self):
        print_("OnInit")
        frm = MyFrame(None, title="Hello with Events", size=(480, 360))
        frm.Show()
        return True

    def OnExit(self):
        print_("OnExit")
        return 0


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == "__main__":
    main()
