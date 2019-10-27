import tkinter as tk
from tkinter import *
from FileShare import fileShare

if __name__ == "__main__":
    obj = tk.Tk()
    obj.title('Share File!')
    obj.geometry("500x500")

    fileShare(obj)
    obj.mainloop() 
