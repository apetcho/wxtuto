#!/usr/bin/env python3
import sys
import os
import platform
import wx


print(wx.version())
print(sys.version)

app = wx.App()
frame = wx.Frame(None, title="Hello World!", size=(400, 275))
panel = wx.Panel(frame)
panel.BackgroundColour = "sky blue"

stext = wx.StaticText(panel, -1, "Hello World!", (15, 10))
stext.SetFont(wx.FFont(14, wx.FONTFAMILY_SWISS, wx.FONTFLAG_BOLD))

stext = wx.StaticText(
    panel, pos=(15, 40),
    label=(
        f"This is wxPython {wx.version()}\nrunning on Python"
        f" {sys.version.split()[0]} {platform.architecture()[0]}"
    )
)
stext.SetFont(wx.FFont(10, wx.FONTFAMILY_SWISS, wx.FONTFLAG_BOLD))

fdir = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(os.path.split(fdir)[0], "images", "phoenix_main.png")
# fname = os.path.join(fdir, "phoenix_main.png")
bitmap = wx.Bitmap(fname)
sbmap = wx.StaticBitmap(panel, bitmap=bitmap, pos=(15, 85))

frame.Show()
app.MainLoop()

