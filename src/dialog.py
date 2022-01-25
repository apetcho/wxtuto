#!/usr/bin/env python3
import wx


class MyDialog(wx.Dialog):

    def __init__(self, *args, **kw):
        super(MyDialog, self).__init__(*args, **kw)

        # Widgets
        text = wx.StaticText(self, label="Hello. I am a Dialog! Hear me roar!")
        okay = wx.Button(self, wx.ID_OK)
        okay.SetDefault()
        cancel = wx.Button(self, wx.ID_CANCEL)

        # Layout
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(text, 0, wx.ALL, 10)
        self.sizer.Add(wx.StaticLine(self), 0, wx.EXPAND)

        # make a new sizer to hold the buttons
        row = wx.BoxSizer(wx.HORIZONTAL)
        row.Add((1, 1), 1)
        row.Add(okay)
        row.Add((1, 1), 1)
        row.Add(cancel)
        row.Add((1, 1), 1)

        # add that sizer to the main sizer
        self.sizer.Add(row, 0, wx.EXPAND|wx.ALL, 10)

        # size the dialog to fit the content managed by the sizer
        self.Fit()


def main():
    app = wx.App()
    dialog = MyDialog(None, title="Hello Dialog")
    _ = dialog.ShowModal()
    dialog.Destroy()
    app.MainLoop()


if __name__ == "__main__":
    main()
