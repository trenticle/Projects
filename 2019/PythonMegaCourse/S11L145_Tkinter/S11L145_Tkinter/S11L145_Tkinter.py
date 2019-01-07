import tkinter
from tkinter import *

newWindow=Tk()

def km_to_miles():
    ##print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)

##b1= Button(newWindow, text= 'Execute')
##b1.pack()
b2= Button(newWindow, text= 'Persevere', command=km_to_miles)
b2.grid(column=0, padx=40)

e1_value=StringVar()
e1= Entry(newWindow, textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(newWindow, height=1, width=20)
t1.grid(row=0, column=2)

newWindow.mainloop()