'''
Created on Apr 26, 2019

@author: TME5
'''
import tkinter
from tkinter.scrolledtext import ScrolledText
w=tkinter.Tk()
w.geometry('500x200')
w.title('Welcome to Tkinter')

txt=ScrolledText(w,width=40,height=1)
txt.insert(tkinter.INSERT,'''Enter Text
This is example 1
This is example 2
This is example 3
''')
txt.grid(column=0,row=1)

w.mainloop()