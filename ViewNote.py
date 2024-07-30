import os
import mimetypes
import send2trash
import tkinter as tk
from tkinter import filedialog, messagebox
from center_window import *
from EditNote import *

from ctypes import windll as ctypes_windll
ctypes_windll.shcore.SetProcessDpiAwareness(1)

width, height = 1000, 175

class ViewNoteWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(bg='#FFFFFF')
        self.title('Workspace Selector')
        self.geometry(f'{width}x{height}')
        center_window(self, width, height)
        
        # Create a frame to cover everything
        self.createNoteFrame = tk.Frame(self, bg='#FFFFFF')
        self.createNoteFrame.pack(expand=True, padx=50, pady=5)

        # Create a label for instructions
        self.viewNoteLabel = tk.Label(self.createNoteFrame, text='Please select the folder that you want it to be a working space.', font='Arial 20', bg='#FFFFFF')
        self.viewNoteLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Create a button to select the folder
        self.selectFolderButton = tk.Button(self.createNoteFrame, text='Select Folder', command=self.selectFolder, font='Arial 20', bg='#FFFFFF')
        self.selectFolderButton.grid(row=1, column=0, padx=10, pady=10)
        
        # Create a cancel button
        self.exitNoteBtn = tk.Button(self.createNoteFrame, text='Cancel', command=self.cancelAction, font='Arial 20', bg='#FFFFFF')
        self.exitNoteBtn.grid(row=1, column=1, padx=10, pady=10)
        
        # Open the ViewNoteListWindow window to show text files
        self.viewNoteListWindow = ViewNoteListWindow()
        self.viewNoteListWindow.withdraw()
    
    def selectFolder(self):
        # Opens a dialog to select a directory
        folder_path = filedialog.askdirectory(parent=self)
        
        if folder_path:
            self.viewNoteListWindow.folder_path = folder_path
            
            # Close this placeholder window
            self.withdraw()
    
    def cancelAction(self):
        # Placeholder for cancel button action; currently does nothing
        pass

class ViewNoteListWindow(tk.Tk):
    def __init__(self, folder_path=None):
        tk.Tk.__init__(self)
        self.configure(bg='#FFFFFF')
        self.title('View Notes')
        self.geometry(f'+{(self.winfo_screenwidth()-width)//2 + 200}+100')
        
        # Create a header label
        header_label = tk.Label(self, text='View Notes', font='Arial 16', bg='#FFFFFF')
        header_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        # Create a warning label
        warning_label = tk.Label(self, text='(Note: only text files appear, NOT binary files)', font='Arial 14', bg='#FFFFFF')
        warning_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        # Put folder path there
        self.folder_path = folder_path
        
        self.editNoteWindow = EditNoteWindow()
        
    @property
    def folder_path(self):
        return self._folder_path
        
    @folder_path.setter
    def folder_path(self, folder_path):
        self._folder_path = folder_path
        
        # If folder_path is not an empty string or not None
        if folder_path:
            # Display the list of .txt files in the folder
            self.display_files()
            
            # Unhide the window
            self.deiconify()
        
    def is_non_binary_file(self, file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type is not None and mime_type.startswith('text')
    
    def display_files(self):
        # Get the list of .txt files in the selected folder
        files = [f for f in os.listdir(self.folder_path) if self.is_non_binary_file(os.path.join(self.folder_path, f))]
        for index, file in enumerate(files):
            file_name_label = tk.Label(self, text=file, font='Arial 12', bg='#FFFFFF')
            file_name_label.grid(row=index+2, column=0, padx=10, pady=5, sticky='w')
            
            # Edit button
            edit_button = tk.Button(self, text='Edit', font='Arial 12', bg='#FFFFFF', command=lambda f=file: self.edit_file(f))
            edit_button.grid(row=index+2, column=1, padx=10, pady=5)
            
            # Delete button
            delete_button = tk.Button(self, text='Delete', font='Arial 12', bg='#FFFFFF', command=lambda f=file: self.delete_file(f))
            delete_button.grid(row=index+2, column=2, padx=10, pady=5)
    
    def edit_file(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        self.editNoteWindow.file_path = file_path
        self.editNoteWindow.editNoteEntry.insert('end', os.path.splitext(file_name)[0])
        self.editNoteWindow.editNoteContent.insert('end', open(file_path).read())
        self.editNoteWindow.viewNoteListWindow = self
        self.withdraw()
        self.editNoteWindow.deiconify()
        
        # os.system(f'notepad.exe "{file_path}"')  # Opens the file with Notepad (Windows)
    
    def delete_file(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        
        # Normalize the file path
        file_path = os.path.normpath(file_path)
        
        # Recycle Bin Delete Confirmation
        if messagebox.askyesno("Delete Confirmation", f"Are you sure you want to move '{file_name}' to the Recycle Bin?"):
            # Move the file to the recycle bin
            send2trash.send2trash(file_path)
            self.refresh_list()
    
    def refresh_list(self):
        # Clear the existing file list
        for widget in self.grid_slaves():
            if int(widget.grid_info()['row']) > 0:
                widget.destroy()
        # Re-display the files
        self.display_files()

if __name__ == '__main__':
    root = tk.Tk()
    app = ViewNoteWindow(root)
    root.mainloop()
