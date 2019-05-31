'''
Created on Apr 26, 2019

@author: TME5
'''
from tkinter import *
w=Tk()
w.geometry('500x200')
w.title('Welcome to Tkinter')

l1=Label(w,text='Testing Label')
l1.grid(column=0,row=0)
chk_state=BooleanVar()
chk_state.set(True)
chk=Checkbutton(w,text='Select',var=chk_state)
chk.grid(column=0,row=1)
w.mainloop()