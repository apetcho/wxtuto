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
        pass

    def resetSelections(self):
        pass

    def onAbout(self, event: wx.Event):
        pass

    def zoomToFit(self, event: wx.Event):
        pass

    def clear(self, event: wx.Event=None):
        pass

    def onQuit(self, event: wx.Event):
        pass

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
