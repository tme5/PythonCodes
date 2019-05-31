'''
Created on Apr 26, 2019

@author: TME5
'''
import tkinter
from tkinter.ttk import *
window=tkinter.Tk()
window.title('Welcome to Tkinter')
window.geometry('500x200')


l1=tkinter.Label(window,text='Testing Label')
l1.grid(column=0,row=0)

combo=Combobox(window)
combo['values']=(1,2,3,4,5,'Text')
combo.current(3)
combo.grid(column=1,row=0)

def clicked():
    l1.config(text=combo.get())
    
b1=tkinter.Button(window,text='Change Label',command=clicked)
b1.grid(column=0,row=1)

window.mainloop()