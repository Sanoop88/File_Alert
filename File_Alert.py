from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import fnmatch
root=Tk()
root.title('FileAlert_new')
frame=Frame(root,height=200,width=300)
frame.grid()

variable=IntVar(root)
variable.set(5)
#you can add more time intervals here, these are in seconds currently, so every 5 seconds, 10 seconds and so on....
varset=[5,10,15,20,25,30,35,40,45,50,55,60,120,300]
w=ttk.OptionMenu(frame,variable,varset[0],*varset)
label=ttk.Label(frame,text='Delay in secs')

var=StringVar()
var.set('Both')

radio1=Radiobutton(frame,text='folder1',variable=var,value='folder1')
radio2=Radiobutton(frame,text='folder2',variable=var,value='folder2')
radio3=Radiobutton(frame,text='Both',variable=var,value='Both')
radio4=Radiobutton(frame,text='None',variable=var,value='None')
label1=ttk.Label(frame,text='Select:-')
label1.grid(row=0,column=3)
radio1.grid(row=2,column=3,sticky='w')
radio2.grid(row=1,column=3,sticky='w')
radio3.grid(row=3,column=3,sticky='w')
radio4.grid(row=4,column=3,sticky='w')


messagebox.showerror('Connection check','Please ensure you have access to the folders before proceeding')


path1='/Users/videoqa/Desktop/xfer ad/encoded/music'
path2='/Users/videoqa/Desktop/xfer ad/Complete'






global Flag
Flag=True


def folder_1():
    #you can define the file extensions you wish to track here, I'm using this to track (mp4, mov, mpg)
    mp4ads=len(fnmatch.filter(os.listdir(path1), '*.mp4'))
    movads=len(fnmatch.filter(os.listdir(path1), '*.mov'))
    mpgads=len(fnmatch.filter(os.listdir(path1), '*.mpg'))
    totalads=mp4ads+movads+mpgads

    if totalads==0:
        pass
    elif totalads==1:
        os.system('Say "One File"')
    else:
        os.system('Say %s Files' %(totalads))
def folder_2():
    #file extensions for second folder
    movmusic=len(fnmatch.filter(os.listdir(path2), '*.mov'))
    mpgmusic=len(fnmatch.filter(os.listdir(path2), '*.mpg'))
    totalmusic=movmusic+mpgmusic
    if totalmusic==0:
        pass
    elif totalmusic==1:
        os.system('Say "One item"')
    else:
        os.system('Say %s items' %(totalmusic))

test=None        
def start():
    if os.path.dir(path1) and os.path.dir(path2):

        global test
        global Flag
        Flag=True
        if Flag==True and var.get()=='Both': 
            folder_1()
            folder_2()

        elif Flag==True and var.get()=='folder1': 
            folder_1()

        elif Flag==True and var.get()=='folder2': 
            folder_2()
        else:
            pass
        test=root.after((variable.get()*1000),start)
    else:
        messagebox.showerror('Connection Lost','Please ensure you have access to the folders before proceeding')

    

def stop():
    global test
    global Flag
    Flag=False
    root.after_cancel(test)

def destroy():
    root.destroy()


button1=ttk.Button(frame,text='Start',command=start)
button2=ttk.Button(frame,text='Stop',command=stop)
button3=ttk.Button(frame,text='End',command=destroy)
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=1,column=0,columnspan=2)
label.grid(row=0,column=2)
w.grid(row=1,column=2)

root.mainloop()





            



