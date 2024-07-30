import tkinter as tk
from center_window import *

from ctypes import windll as ctypes_windll
ctypes_windll.shcore.SetProcessDpiAwareness(1)

width, height = 600, 200

class HomeWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='#FFFFFF')
        self.title("Home Page - Noble's Notepad")
        self.geometry(f"{width}x{height}")
        center_window(self, width, height)

        self.homeFrame = tk.Frame(self, bg='#FFFFFF')

        self.homeLabel = tk.Label(self.homeFrame, text='Home', font='Arial 20', bg='#FFFFFF')
        self.homeLabel.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

        self.createNoteBtn = tk.Button(self.homeFrame, text='Create Note', font='Arial 20', bg='#FFFFFF')
        self.createNoteBtn.grid(column=0, row=1, padx=15, pady=30)

        self.viewNoteBtn = tk.Button(self.homeFrame, text='View Notes', font='Arial 20', bg='#FFFFFF')
        self.viewNoteBtn.grid(column=1, row=1, padx=15, pady=30)

        self.homeFrame.pack(expand=True, padx=50, pady=5)
        
if __name__ == '__main__':
    homeWindow = HomeWindow()
    homeWindow.mainloop()