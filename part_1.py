from tkinter import *
import tkinter
from tkinter import filedialog
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


def dialog_box():
    root.filename = filedialog.askopenfilename(initialdir="/", title="choose your file",filetypes=(("all files", "*.*"),("all files", "*.*")))
    label = Label(root, text= root.filename,fg='#8B0000',height='1',width='100',relief=RAISED)
    label.pack()

B = tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Select File",command = dialog_box,width=20)
B.pack(side=TOP, padx=45, pady=5)
B= tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Establish Connection",width=20)
B.pack(side=LEFT, padx=40, pady=15)
B = tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Abort Connection and Quit",command= quit,width=20)
B.pack(side=RIGHT, padx=40, pady=15)

root.mainloop()
