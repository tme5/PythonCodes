'''
Created on Apr 26, 2019

@author: TME5
'''
import tkinter
window=tkinter.Tk()
window.geometry('500x200')
window.title('Welcome to Tkinter')
l1=tkinter.Label(window,text='Testing Entry')
l1.grid(column=0,row=0)

txt=tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)

def clicked():
    res="Welcome to "+txt.get()
    l1.config(text=res)

b1=tkinter.Button(window,text='Change',fg='white',bg='red',command=clicked)
b1.grid(column=0,row=1)

window.mainloop()