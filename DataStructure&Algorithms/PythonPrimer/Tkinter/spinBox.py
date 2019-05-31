'''
Created on Apr 26, 2019

@author: TME5
'''

from tkinter import messagebox
def clicked():
    messagebox.showinfo('Value',spin.get())
    
from tkinter import *
w=Tk()
w.geometry('500x200')
w.title('Welcome to Tkinter')

spin=Spinbox(w,from_=0,to=100,width=5)
spin.grid(column=0,row=0)

b1=Button(w,text='Button1',command=clicked)
b1.grid(column=0,row=1)

w.mainloop()