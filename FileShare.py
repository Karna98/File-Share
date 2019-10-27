import os
import shutil
import sys
import tkinter as tk
import urllib.request
import webbrowser
import socket
from subprocess import Popen 
from tkinter import *
from tkinter import filedialog

class fileShare:
    def __init__(self, obj):
        self.obj = obj
        self.currentWrokingDir = os.getcwd()
        if os.name == 'nt':
            self.fileCacheDir = self.currentWrokingDir + '\\fileCache'
        else:
            self.fileCacheDir = self.currentWrokingDir + '/fileCache'
        self.subProcessId = ''
        self.homeFrame()

    def all_children (self, window) :
        _list = window.winfo_children()
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        return _list

    def clear_window(self, window):
        widget_list = all_children(window)

    def change_frame(self, which_frame, from_which_frame):
        from_which_frame.destroy()
        which_frame()

    def go(self, textBox):
        inputValue = textBox.get("1.0", "end-1c")
        inputValue = 'http://' + inputValue
        print(inputValue)
        webbrowser.open( inputValue )

    def selectFiles(self, frame):
        os.makedirs("fileCache", exist_ok=True)
        frame.filename = filedialog.askopenfilename(initialdir = self.currentWrokingDir, title="choose your file",filetypes=(("all files", "*.*"),("all files", "*.*")))
        if (frame.filename != ''):
            label = Label(frame, text = frame.filename, height='1', width='100', relief=RAISED)
            shutil.copy2(frame.filename, 'fileCache')
            label.pack()

    def closeConnection(self):
        self.subProcessId.kill()
        if ( not os._exists(self.fileCacheDir) ):
            shutil.rmtree(self.fileCacheDir)
        quit()

    def establishConnection(self, frame): 
        self.subProcessId = Popen("cd 1" + self.fileCacheDir + " && python -m http.server",shell=True) 
        print(self.subProcessId)
        label = Label(frame, text = 'Connection Established to 192.168.0.101:8080 !!')
        label.pack()

    def homeFrame(self):
        frame = Frame(self.obj, width = 500, height = 500)
        frame.pack(pady = 80)

        b1 = Button(frame, width = 20, bd = 5, text ="Send", command = lambda : self.change_frame(lambda : self.sendFrame(self.obj), frame))
        b1.pack(pady = 20)

        b2 = Button(frame, width = 20, bd = 5, text ="Receive", command = lambda : self.change_frame(lambda : self.receiveFrame(self.obj), frame))
        b2.pack(pady = 20)

        b3 = Button(frame, width = 20, bd = 5, text ="Quit", command = quit)
        b3.pack(pady = 20)

    def sendFrame(self, obj):
        self.get_Host_name_IP()
        frame = Frame(obj, width = 500, height = 500)
        frame.pack(pady=80)

        b1 = Button(frame, width = 20, bd = 5, text = "Select File", command = lambda : self.selectFiles(frame))
        b1.pack(pady = 5)

        b2 = Button(frame, width = 20, bd = 5, text = "Establish Connection",command = lambda : self.establishConnection(frame))
        b2.pack(pady = 15)

        b3 = Button(frame, width = 20, bd = 5, text = "Quit", command = self.closeConnection)
        b3.pack(pady = 15)

    def receiveFrame(self, obj):
        frame = Frame(obj, width = 500, height = 500)
        frame.pack(pady = 80)

        l = Label(frame, text = 'Enter URL shared by Sender (ex. 127.0.0.101:8000)')
        l.pack(pady=20)

        textBox=Text(frame, height = 1, width = 20)
        textBox.pack()

        b1 = Button(frame, width = 20, bd = 5, text = 'Go', command = lambda : self.go(textBox))
        b1.pack(pady = 10)

        b2 = Button(frame, width = 20, bd = 5, text = 'Back', command = lambda : self.change_frame(lambda : self.homeFrame(), frame))
        b2.pack(pady = 10)
