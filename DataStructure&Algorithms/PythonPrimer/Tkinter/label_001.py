#!python
'''
Created on Apr 26, 2019

@author: TME5
'''
import tkinter
window=tkinter.Tk()
window.title("Welcome to Tkinter")
l1=tkinter.Label(window,text="Testing Label", font=("Arial Bold",50))
l1.grid(column=0,row=0)

window.geometry('500x200')
window.mainloop()
