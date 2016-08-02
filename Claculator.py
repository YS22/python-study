from Tkinter import *
root=Tk()
root.title('Claculator')
display=StringVar()
Entry(root,textvariable=display).pack(side=TOP,expand=YES,fill=BOTH)
line=Frame(root)
line.pack(side=TOP,expand=YES,fill=BOTH)
line1=Frame(root)
line1.pack(side=TOP,expand=YES,fill=BOTH)
line2=Frame(root)
line2.pack(side=TOP,expand=YES,fill=BOTH)
line3=Frame(root)
line3.pack(side=TOP,expand=YES,fill=BOTH)
line4=Frame(root)
line4.pack(side=TOP,expand=YES,fill=BOTH)
for key in '123':
	Button(line,text=key,command=lambda w=display,s=key:w.set(w.get()+s)).pack(side=LEFT,expand=YES,fill=BOTH)
for key1 in '456':
	Button(line1,text=key1,command=lambda w=display,s=key1:w.set(w.get()+s)).pack(side=LEFT,expand=YES,fill=BOTH)
for key2 in '789':
	Button(line2,text=key2,command=lambda w=display,s=key2:w.set(w.get()+s)).pack(side=LEFT,expand=YES,fill=BOTH)
for key3 in '+-*/':
	Button(line3,text=key3,command=lambda w=display,s=key3:w.set(w.get()+s)).pack(side=LEFT,expand=YES,fill=BOTH)
Button(line4,text='Clr',command=lambda w=display:w.set('')).pack(side=LEFT,expand=YES,fill=BOTH)
Button(line4,text='=',command=lambda w=display:w.set(eval(w.get()))).pack(side=LEFT,expand=YES,fill=BOTH)
root.mainloop()
'''
from Tkinter import *
root=Tk()
w=StringVar()
w.set(1+2+3)
print eval(w.get())
'''