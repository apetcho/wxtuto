#!/usr/bin/env python3
"""
A simple test to verify that the GIL is released while in long running wrappers
like MainLoop, ShowModal, and PopupMenu so background threads can be allowed
to run at those times.
"""
import wx
import threading
import time
import random


class ThreadedTask(threading.Thread):

    def __init__(self, *args, **kwargs):
        pass

    def run(self):
        pass


class MainFrame(wx.Frame):
    def __init__(self):
        pass

    def onButton(self, event):
        pass

    def onOtherButton(self, event):
        pass

    def onShowMenu(self, event):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
