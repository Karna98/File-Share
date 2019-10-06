import tkinter as tk
from tkinter import *
import BackBone as bB

if __name__ == "__main__":
    obj = tk.Tk()
    obj.title('Share File!')
    obj.geometry("500x500")

    bB.homeFrame(obj)    
    obj.mainloop() 
