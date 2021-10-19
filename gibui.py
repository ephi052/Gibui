import tkinter as tk
from tkinter import StringVar, ttk, filedialog as fd
from tkinter.messagebox import showinfo
from dirsync import sync

SorceFolder = ""
TargetFolder = ""

root = tk.Tk()
root.title('GIBUI')
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')


def select_file_ss():
    SF = fd.askdirectory()
    sorceFolderEntery.insert(0, SF)


def select_file_st():
    TF = fd.askdirectory()
    targetFolderEntery.insert(0, TF)


def check():
    if not checkInputs() != True:
        sync(theSourceFolder.get(), theTargetFolder.get(), 'diff', )


def syncCommand():
    if not checkInputs() != True:
        sync(theSourceFolder.get(), theTargetFolder.get(), 'sync', )


def checkInputs():
    if theSourceFolder.get() == "" or theTargetFolder.get() == "":
        showinfo(title='Info', message='Select Folders Path')
        return False
    else:
        return True


btSize = 30
sorceFolder = ttk.Button(root, text='Select Source', command=select_file_ss)
sorceFolder.grid(column=0, row=1, ipadx=btSize)

targetFolder = ttk.Button(root, text='Select Target', command=select_file_st)
targetFolder.grid(column=0, row=2, ipadx=btSize)

checkBt = ttk.Button(root, text='Check', command=check)
checkBt.grid(column=0, row=3, ipadx=btSize)

backupBt = ttk.Button(root, text='sync', command=syncCommand)
backupBt.grid(column=1, row=3, ipadx=75, columnspan=2)

theSourceFolder = StringVar()
sorceFolderEntery = tk.Entry(root, textvariable=theSourceFolder)
sorceFolderEntery.grid(column=1, row=1, ipadx=75, columnspan=2)

theTargetFolder = StringVar()
targetFolderEntery = tk.Entry(root, textvariable=theTargetFolder)
targetFolderEntery.grid(column=1, row=2, ipadx=75, columnspan=2)

root.mainloop()