#!/usr/bin/env python3
import wx

USE_WIT = False
AppBaseClass = wx.App
if USE_WIT:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp


class MyFrame(wx.Frame):
    """This is MyFrame. It just shows a few controls on a wxPanel, and
    has simple menu.
    """

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, -1, title)

        # Create the menubar
        menubar = wx.MenuBar()

        # and a menu
        menu = wx.Menu()

        # Add an item to the menu, using \tKeyName automatically creates
        # an accelerator, the third param is some help text that will
        # show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bin the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menubar.Append(menu, "&File")
        self.SetMenuBar(menubar)

        self.CreateStatusBar()

        # Now create the Panel to put the other controls on.
        panel = wx.Panel(self)

        # and a few controls
        text = wx.StaticText(panel, -1, "Hello World! Welcome to wxPython.")
        text.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD))
        text.SetSize(text.GetBestSize())
        btn = wx.Button(panel, -1, "Close")
        funbtn = wx.Button(panel, -1, "Just for fun...")

        # bind the button events to handlers
        self.Bind(wx.EVT_BUTTON, self.OnTimeToClose, btn)
        self.Bind(wx.EVT_BUTTON, self.OnFunButton, funbtn)

        # Use a size to layout the controls, stacked vertically and with
        # a 10 pixel border around each
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 10)
        sizer.Add(btn, 0, wx.ALL, 10)
        sizer.Add(funbtn, 0, wx.ALL, 10)
        panel.SetSizer(sizer)
        panel.Layout()

        # And also use a sizer ot manage the size of the panel such that it
        # fills the frame
        sizer = wx.BoxSizer()
        sizer.Add(panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Fit()
        self.CenterOnScreen(wx.BOTH)

    def OnTimeToClose(self, event):
        """Event handler for the button click"""
        print("See ya later!")
        self.Close()

    def OnFunButton(self, event):
        """Event handler for the button click."""
        print("Having fun yet?")


class MyApp(AppBaseClass):
    def OnInit(self):
        pass


def main():
    app = MyApp(redirect=True)
    app.MainLoop()


if __name__ == "__main__":
    main()
