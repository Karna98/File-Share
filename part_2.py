import tkinter
import subprocess
import urllib.request
import webbrowser
from tkinter import *
from PIL import ImageTk , Image


root = tkinter.Tk()
root.title("Share File!")
root.geometry("500x500")
root.configure(background='#CD8C95')

canvas = Canvas(root, width = 500, height = 250)
line = canvas.create_line(0,251,500,251)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("icon.jpg"))
canvas.create_image(0, 0, anchor=NW, image=img)

def go():
    inputValue = textBox.get("1.0", "end-1c")
    print(inputValue)
    webbrowser.open(inputValue)

label = Label(root, text= 'Enter URL shared by Sender(ex. 127.0.0.101:8000)')
label.pack(side=TOP,padx=30,pady=20)

textBox=Text(root, height=1, width=20)
textBox.pack()

button = Button(root,bd = 5,bg= '#FFB6C1', text='Go', command =  lambda: go())
button.pack(side=TOP, padx=45, pady=10)

button = Button(root,bd = 5,bg= '#FFB6C1', text='Quit Application :-(', command =  quit)
button.pack(side=TOP, padx=45, pady=10)

root.mainloop()