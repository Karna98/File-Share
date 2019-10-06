import os
import shutil
import sys
import tkinter as tk
import urllib.request
import webbrowser

from tkinter import *
from tkinter import filedialog

currentWrokingDir = os.getcwd()
if os.name == 'nt':
    fileCacheDir = currentWrokingDir + '\\fileCache'
else:
    fileCacheDir = currentWrokingDir + '/fileCache'

def all_children (window) :
    _list = window.winfo_children()
    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())
    return _list

def clear_window(window):
    widget_list = all_children(window)

def change_frame(obj,which_frame,from_which_frame):
    from_which_frame.destroy()
    which_frame()

def go(textBox):
    inputValue = textBox.get("1.0", "end-1c")
    inputValue = 'http://' + inputValue
    print(inputValue)
    webbrowser.open( inputValue )

def selectFiles(frame):
    os.makedirs("fileCache", exist_ok=True)
    frame.filename = filedialog.askopenfilename(initialdir = currentWrokingDir, title="choose your file",filetypes=(("all files", "*.*"),("all files", "*.*")))
    label = Label(frame, text = frame.filename, height='1', width='100', relief=RAISED)
    shutil.copy2(frame.filename, 'fileCache')
    label.pack()

def closeConnection():
    if ( not os._exists(fileCacheDir) ):
        shutil.rmtree(fileCacheDir)
    quit()

def establishConnection(frame): 
    if( os.system("cd " + fileCacheDir + " && python -m http.server") ):
        label = Label(frame, text = 'Connection Established to 192.168.0.101:8080 !!')
        label.pack()
    else:
        label = Label(frame, text = 'Connection Failed!!')
        label.pack()

def homeFrame(obj):
    frame = Frame(obj, width = 500, height = 500)
    frame.pack(pady = 80)

    b1 = Button(frame, width = 20, bd = 5, text ="Send", command = lambda : change_frame(obj, lambda : sendFrame(obj), frame))
    b1.pack(pady = 20)

    b2 = Button(frame, width = 20, bd = 5, text ="Receive", command = lambda : change_frame(obj, lambda:receiveFrame(obj), frame))
    b2.pack(pady = 20)

    b3 = Button(frame, width = 20, bd = 5, text ="Quit", command = quit)
    b3.pack(pady = 20)

def sendFrame(obj):
    frame = Frame(obj, width = 500, height = 500)
    frame.pack(pady=80)

    b1 = Button(frame, width = 20, bd = 5, text = "Select File", command = lambda : selectFiles(frame))
    b1.pack(pady = 5)

    b2 = Button(frame, width = 20, bd = 5, text = "Establish Connection",command = lambda : establishConnection(frame))
    b2.pack(pady = 15)

    b3 = Button(frame, width = 20, bd = 5, text = "Quit", command = closeConnection)
    b3.pack(pady = 15)

def receiveFrame(obj):
    frame = Frame(obj, width = 500, height = 500)
    frame.pack(pady = 80)

    l = Label(frame, text = 'Enter URL shared by Sender (ex. 127.0.0.101:8000)')
    l.pack(pady=20)

    textBox=Text(frame, height = 1, width = 20)
    textBox.pack()

    b1 = Button(frame, width = 20, bd = 5, text = 'Go', command = lambda : go(textBox))
    b1.pack(pady = 10)

    b2 = Button(frame, width = 20, bd = 5, text = 'Back', command = lambda : change_frame(obj, lambda : homeFrame(obj), frame))
    b2.pack(pady = 10)
