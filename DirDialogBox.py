from tkinter import * 
from tkinter import filedialog

def loc_browser():
    root = Tk()
    root.filename = filedialog.askdirectory(title='Select New Backup Location')
    if root.filename == '':                                 # if nothing is selected an emty bulocks file is created
        with open('bulocks.txt', 'a') as locations:
            pass
    else:                                                   # if a directory is selected it is added to newly/already created bulocks file
        with open('bulocks.txt', 'a') as locations:
            locations.write(f'{root.filename}\n')
    root.destroy()
    return root.filename

