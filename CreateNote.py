import tkinter as tk
from tkinter import filedialog, messagebox
from center_window import *

from ctypes import windll as ctypes_windll
ctypes_windll.shcore.SetProcessDpiAwareness(1)

width, height = 1100, 870

class CreateNoteWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='#FFFFFF')
        self.title("Create New Note - Noble's Notepad")
        self.geometry(f"{width}x{height}")
        center_window(self, width, height)

        # Create a frame to cover everything
        self.createNoteFrame = tk.Frame(self, bg='#FFFFFF')
        self.createNoteFrame.pack(expand=True, padx=50, pady=5)

        # Create a Create Note Window Title
        self.createNoteWindowTitle = tk.Label(self.createNoteFrame, text='Create Note', font='Arial 20', bg='#FFFFFF')
        self.createNoteWindowTitle.grid(column=0, row=0, columnspan=2)

        # Create a Create Note Title Label
        self.createNoteTitle = tk.Label(self.createNoteFrame, text='Note Title (up to 30 characters):', font='Arial 16', bg='#FFFFFF', anchor='w')
        self.createNoteTitle.grid(column=0, row=1, columnspan=2, sticky='w')

        # Create a Create Note Title Entry
        self.createNoteEntry = tk.Entry(self.createNoteFrame,
                                        font='Arial 12',
                                        bg='#FFFFFF',
                                        validate="key",
                                        validatecommand=(self.register(lambda text: len(text) <= 30), "%P")
        )
        self.createNoteEntry.grid(column=0, row=2, columnspan=2, sticky='nsew')

        # Create a Create Note Content Label
        self.createNoteLabel = tk.Label(self.createNoteFrame, text='\nNote Content:', font='Arial 16', bg='#FFFFFF', anchor='w')
        self.createNoteLabel.grid(column=0, row=3, columnspan=2, sticky='w')

        # Create a Create Note Content Textbox
        self.createNoteContent = tk.Text(self.createNoteFrame, font='Arial 12', bg='#FFFFFF')
        self.createNoteContent.grid(column=0, row=4, columnspan=2, sticky='nsew')

        # Create a Save Note Button
        self.saveNoteBtn = tk.Button(self.createNoteFrame, text='Save', font='Arial 20', bg='#FFFFFF', command=self.saveFile)
        self.saveNoteBtn.grid(column=0, row=5, padx=15, pady=30)

        # Create an Exit Note Button
        self.exitNoteBtn = tk.Button(self.createNoteFrame, text='Cancel', font='Arial 20', bg='#FFFFFF')
        self.exitNoteBtn.grid(column=1, row=5, padx=15, pady=30)
        
    def saveFile(self):
        # Get the title from the Entry widget
        title = self.createNoteEntry.get()
        
        # Open the file save dialog
        file_path = filedialog.asksaveasfilename(parent=self,
                                                 initialfile=title,
                                                 defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            # Get the content from the Text widget
            file_content = self.createNoteContent.get(1.0, tk.END)
            
            # Write the content to the file
            with open(file_path, 'w') as file:
                file.write(file_content)
                
            messagebox.showinfo('Saved', 'File has successfully been saved!\nNote: Click "OK" will only go back here. Click "Cancel" again after that to return to homepage.', parent=self)

if __name__ == '__main__':
    createNoteWindow = CreateNoteWindow()
    createNoteWindow.mainloop()