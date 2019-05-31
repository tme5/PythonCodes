'''
Created on Apr 26, 2019

@author: TME5
'''
from tkinter import *
w=Tk()
w.geometry('500x200')
w.title('Welcome to Tkinter')

rad1=Radiobutton(w,text='Python',value=1)
rad2=Radiobutton(w,text='Shell',value=2)
rad3=Radiobutton(w,text='DOS',value=3)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
w.mainloop()
