'''
Created on Apr 26, 2019

@author: TME5
'''
from tkinter import messagebox
def clicked():
    messagebox.showinfo('Message tile','Hello Tushar')
from tkinter import *
w=Tk()
w.geometry('500x200')
w.title('Welcome to Tkinter')
b1=Button(text='Button1',command=clicked)
b1.grid(column=0,row=0)

w.mainloop()
