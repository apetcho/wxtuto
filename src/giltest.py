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
        super(ThreadedTask, self).__init__(*args, **kwargs)
        self.counter = 0
        self.sleepTime = random.random()/2
        self.timeToDie = False

    def run(self):
        while not self.timeToDie:
            time.sleep(self.sleepTime)
            self.counter += 1
            print(f"thread: {self.name:5s} count: {self.counter:d}")


class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None, title="GIL Test")
        self.panel = wx.Panel(self)
        button = wx.Button(self.panel, label="modal dialog", pos=(10, 10))
        self.Bind(wx.EVT_BUTTON, self.onButton, button)
        self.panel.Bind(wx.EVT_CONTEXT_MENU, self.onShowMenu)
        button = wx.Button(self.panel, label="timed test", pos=(10, 60))
        self.Bind(wx.EVT_BUTTON, self.onOtherButton, button)

    def onButton(self, event):
        dialog = wx.Dialog(self, title="close this dialog", size=(300, 150))
        dialog.ShowModal()
        dialog.Destroy()

    def onOtherButton(self, event):
        # A simplistic benchmark test that times many repetitions of some
        # simple operations so they can be tested with and without releasing
        # the GIL
        start = time.time()
        reps = 100000
        for _ in range(reps):
            size = wx.Size(100, 100)
            for _ in range(10):
                size.DecBy(4, 6)
            for _ in range(10):
                size.IncBy(4, 6)
        wx.MessageBox(
            f"{reps:d} reps performed in {(time.time()-start):f}",
            "Results"
        )

    def onShowMenu(self, event):
        menu = wx.Menu()
        menu.Append(-1, "one")
        menu.Append(-1, "two")
        menu.Append(-1, "three")
        self.panel.PopupMenu(menu)
        menu.Destroy()


def main():
    threads = [
        ThreadedTask(name="one"),
        ThreadedTask(name="two"),
        ThreadedTask(name="three")
    ]
    for t in threads:
        t.start()

    app = wx.App()
    frm = MainFrame()
    frm.Show()
    app.MainLoop()

    for t in threads:
        t.timeToDie = True


if __name__ == "__main__":
    main()
