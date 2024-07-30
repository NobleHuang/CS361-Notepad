from Home import *
from EditNote import *
from ViewNote import *
from CreateNote import *

homeWindow = HomeWindow()
createNoteWindow = CreateNoteWindow()
viewNoteWindow = ViewNoteWindow()

createNoteWindow.withdraw()
viewNoteWindow.withdraw()
viewNoteWindow.viewNoteListWindow.editNoteWindow.withdraw()
    
def createNoteCancel():
    # if 'createNoteWindow' in globals():
    createNoteWindow.withdraw()
    homeWindow.deiconify()
    
def editNoteCancel():
    # if 'editNoteWindow' in globals():
    viewNoteWindow.viewNoteListWindow.editNoteWindow.withdraw()
    viewNoteWindow.viewNoteListWindow.deiconify()
    
def createNoteFunc():
    homeWindow.withdraw()
    createNoteWindow.deiconify()
    
def viewNoteCancel():
    # if 'viewNoteWindow' in globals():
    viewNoteWindow.withdraw()
    homeWindow.deiconify()
    
def viewNoteListCancel():
    # if 'viewNoteWindow' in globals():
    viewNoteWindow.viewNoteListWindow.withdraw()
    homeWindow.deiconify()
    
def viewNoteFunc():
    homeWindow.withdraw()
    viewNoteWindow.deiconify()

homeWindow.protocol('WM_DELETE_WINDOW', lambda: homeWindow.destroy() )

createNoteWindow.exitNoteBtn['command'] = createNoteCancel
viewNoteWindow.viewNoteListWindow.editNoteWindow.exitNoteBtn['command'] = editNoteCancel
viewNoteWindow.exitNoteBtn['command'] = viewNoteCancel

createNoteWindow.protocol('WM_DELETE_WINDOW', createNoteCancel)
viewNoteWindow.protocol('WM_DELETE_WINDOW', viewNoteCancel)
viewNoteWindow.viewNoteListWindow.protocol('WM_DELETE_WINDOW', viewNoteListCancel)

# Implement monkey patching into the CreateNote Button
homeWindow.createNoteBtn['command'] = createNoteFunc

# Implement monkey patching into the ViewNote Button
homeWindow.viewNoteBtn['command'] = viewNoteFunc

homeWindow.mainloop()