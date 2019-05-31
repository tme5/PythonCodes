#!python
'''
Created on Apr 26, 2019

@author: TME5
'''
def clicked():
    l1.configure(text="Button was clicked !!!")


import tkinter
window=tkinter.Tk()
window.title("Welcome to Tkinter")
l1=tkinter.Label(window,text="Testing Label")
l1.grid(column=0,row=0)
b1=tkinter.Button(window,text='Button1',bg='orange',fg='green',command=clicked)
b1.grid(column=0,row=1)

window.geometry('500x200')
window.mainloop()