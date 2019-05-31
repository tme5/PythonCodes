'''
Created on Apr 30, 2019

@author: TME5
'''
import sys
from tkinter import *

root=Tk()
#root.geometry('240x584')
root.title('pyCalculator')

def pyInsert(ent,val):
    ent.insert(END,val)

def pyClear1(ent):
    ent.delete(0,END)
def makeForm(root,choice):
    if choice == 'Std':
        pyDisp=Entry(root,justify='right',width=50)
        pyDisp.grid(row=0,column=0,sticky='we',pady=1,padx=1,columnspan=5,ipady=4)
        Button(root,text='C',width=10).grid(row=1,column=0,padx=1,pady=1)
        Button(root,text='CE',width=10).grid(row=1,column=1,padx=1,pady=1)
        Button(root,text='±',width=10).grid(row=1,column=2,padx=1,pady=1)
        Button(root,text='√',width=10).grid(row=1,column=3,padx=1,pady=1)
        Button(root,text='x²',width=10).grid(row=1,column=4,padx=1,pady=1)
        
        Button(root,text='7',width=10,command=pyInsert(pyDisp,'7')).grid(row=2,column=0,padx=1,pady=1)
        Button(root,text='8',width=10).grid(row=2,column=1,padx=1,pady=1)
        Button(root,text='9',width=10).grid(row=2,column=2,padx=1,pady=1)
        Button(root,text='/',width=10).grid(row=2,column=3,padx=1,pady=1)
        Button(root,text='%',width=10).grid(row=2,column=4,padx=1,pady=1)
        
        Button(root,text='4',width=10).grid(row=3,column=0,padx=1,pady=1)
        Button(root,text='5',width=10).grid(row=3,column=1,padx=1,pady=1)
        Button(root,text='6',width=10).grid(row=3,column=2,padx=1,pady=1)
        Button(root,text='*',width=10).grid(row=3,column=3,padx=1,pady=1)
        Button(root,text='1/x',width=10).grid(row=3,column=4,padx=1,pady=1)
        
        Button(root,text='1',width=10).grid(row=4,column=0,padx=1,pady=1)
        Button(root,text='2',width=10).grid(row=4,column=1,padx=1,pady=1)
        Button(root,text='3',width=10).grid(row=4,column=2,padx=1,pady=1)
        Button(root,text='-',width=10).grid(row=4,column=3,padx=1,pady=1)
        Button(root,text='=',width=10,height=3).grid(row=4,column=4,rowspan=2,padx=1,pady=1)
        
        Button(root,text='0',width=22).grid(row=5,column=0,columnspan=2,padx=1,pady=1)
        Button(root,text='.',width=10).grid(row=5,column=2,padx=1,pady=1)
        Button(root,text='+',width=10).grid(row=5,column=3,padx=1,pady=1)

def pyStdCalc():
    makeForm(root,'Std')
    root.grid_columnconfigure(0, weight=0)
    root.resizable(False, False)
    
def pySciCalc():
    root.geometry('480x284')
    

#+----{ Menu bar setup }----+
vlevel=IntVar()
vlevel.set(1)
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_radiobutton(label='Standard',command=pyStdCalc,variable=vlevel,value=1)
filemenu.add_radiobutton(label='Scientific',command=pySciCalc,variable=vlevel,value=2)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=sys.exit)
menubar.add_cascade(label='File',menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
menubar.add_cascade(label='Edit',menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='About')
menubar.add_cascade(label='Help',menu=helpmenu)

root.config(menu=menubar)
pyStdCalc()
root.mainloop()

