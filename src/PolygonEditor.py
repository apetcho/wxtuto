#!/usr/bin/env python3
"""PolygonEditor: a simple app for editing polygons

Used as a demo for FloatCanvas.
"""
import numpy as np
import random
import numpy.random as RandomArray

import wx
from wx.lib.floatcanvas import NavCanvas, FloatCanvas


class DrawFrame(wx.Frame):
    """A frame used for the Floatcanvas Demo."""

    def __init__(self, parent, id, title, position, size):
        super(DrawFrame, self).__init__(parent, id, title, position, size)

        # Set up the menubar
        menubar = wx.MenuBar()

        # -- file menu
        fmenu = wx.Menu()
        exit = fmenu.Append(wx.ID_EXIT, "", "Close Application")
        self.Bind(wx.EVT_MENU, self.onQuit, exit)

        menubar.Append(fmenu, "&File")

        # View menu
        vmenu = wx.Menu()
        zfit = vmenu.Append(wx.ID_ANY, "Zoom to &Fit", "Zoom to fit the window")
        self.Bind(wx.EVT_MENU, self.zoomToFit, zfit)
        menubar.Append(vmenu, "&View")

        # Help menu
        hmenu = wx.Menu()
        about = hmenu.Append(
            wx.ID_ABOUT, "", "More information About this program"
        )
        self.Bind(wx.EVT_MENU, self.onAbout, about)
        menubar.Append(hmenu, "&Help")

        self.SetMenuBar(menubar)
        self.CreateStatusBar()

        # Add the Canvas
        self.canvas = NavCanvas.NavCanvas(
            self, -1, (500, 500), Debug=0,
            BackgroundColor="DARK SLATE BLUE"       
        ).Canvas
        self.Bind(wx.EVT_CLOSE, self.onCloseWindow)

        self.canvas.Bind(FloatCanvas.EVT_MOTION, self.onMove)
        self.canvas.Bind(FloatCanvas.EVT_LEFT_UP, self.onLeftUp)
        self.canvas.Bind(FloatCanvas.EVT_LEFT_DOWN, self.onLeftClick)

        self.resetSelections()

    def resetSelections(self):
        self.selectedPolygon = None
        self.selectedPoygonOrig = None
        self.selectedPoints = None
        self.pointSelected = False
        self.selectedPointNeighbors = None

    def onAbout(self, event: wx.Event):
        dialog = wx.MessageDialog(
            self,
            (
                "This is a small program to demonstrate\n"
                "the use of the FloatCanvas\n"
            ),
            "About Me", wx.OK | wx.ICON_INFORMATION
        )
        dialog.ShowModal()
        dialog.Destroy()

    def zoomToFit(self, event: wx.Event):
        self.canvas.ZoomToBB()

    def clear(self, event: wx.Event=None):
        self.canvas.ClearAll()
        self.canvas.SetProjectionFun(None)
        self.canvas.Draw()

    def onQuit(self, event: wx.Event):
        self.Close(True)

    def onCloseWindow(self, event: wx.Event):
        pass

    def onMove(self, event: wx.Event):
        pass

    def onLeftUp(self, event: wx.Event):
        pass

    def onLeftClick(self, event: wx.Event):
        pass

    def setup(self, event: wx.Event=None):
        pass

    def selectPolygon(self, obj):
        pass

    def deselectPolygon(self):
        pass

    def selectPointHit(self, pointSet):
        pass


class PolygonEditor(wx.App):
    """A simple example of making editable shapes with FloatCanvas."""

    def OnInit(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
