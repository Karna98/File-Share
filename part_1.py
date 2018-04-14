import tkinter
import shutil
import os,sys
from tkinter import *
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

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print (proc_stdout)

def dialog_box():
    root.filename = filedialog.askopenfilename(initialdir="/", title="choose your file",filetypes=(("all files", "*.*"),("all files", "*.*")))
    label = Label(root, text= root.filename,fg='#8B0000',height='1',width='100',relief=RAISED)
    shutil.copy2(root.filename, 'SEND-FILES')
    label.pack()

def close_c():
    shutil.rmtree('SEND-FILES')
    quit()

def esta_c():
    patha = os.system("cd D:/py_pro/ROUGH/SEND-FILES && D: && python -m http.server")
    if(patha==0):
        label = Label(root, text='Connection Established to 192.168.0.101:8080 !!')
        label.pack()
    else:
        label = Label(root, text='Connection Failed!!')
        label.pack()

os.makedirs("SEND-FILES", exist_ok=True)

B = tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Select File",command = dialog_box,width=20)
B.pack(side=TOP, padx=45, pady=5)

B= tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Establish Connection",command = esta_c,width=20)
B.pack(side=LEFT, padx=40, pady=15)

B = tkinter.Button(root,bd = 5,bg= '#FFB6C1', text ="Abort Connection and Quit",command= close_c,width=20)
B.pack(side=RIGHT, padx=40, pady=15)

root.mainloop()
