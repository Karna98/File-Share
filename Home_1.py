import tkinter
import subprocess
from tkinter import *
from PIL import ImageTk,Image

root = tkinter.Tk()
root.title("Share File!")
root.geometry("500x500")
root.configure(background='#CD8C95')

canvas = Canvas(root, width = 500, height = 250)
line = canvas.create_line(0,251,500,251)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("icon.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

def call_send():
    subprocess.call(" python part_1.py 1", shell=True)
    quit()

def call_receive():
    subprocess.call(" python part_2.py 1", shell=True)
    quit()

B = tkinter.Button(root,bg= '#FFB6C1',bd = 5, text ="Send a file",command = call_send,width = 20)
B.pack(side=LEFT, padx=50, pady=5)

B = tkinter.Button(root,bg= '#FFB6C1',bd = 5, text ="Receive a file",command = call_receive,width=20)
B.pack(side=RIGHT, padx=50, pady=5)

root.mainloop()