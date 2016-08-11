
import numpy as np 
from Tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure




def drawpic():
	drawpic.f.clf()
	drawpic.a=drawpic.f.add_subplot(111)
	x=np.arange(0,20,0.1)
	y=eval(display.get())

	print y
	drawpic.a.plot(x,y)
	drawpic.canvas.show()

if __name__=='__main__':
	matplotlib.use('TkAgg')
	root=Tk()
	root.title('wan neng hui tu ')
	drawpic.f=Figure(figsize=(5,4),dpi=100)
	drawpic.canvas=FigureCanvasTkAgg(drawpic.f,master=root)
	drawpic.canvas.get_tk_widget().pack(side=TOP,expand=YES,fill=BOTH)

	display=StringVar()
	Entry(root,textvariable=display).pack(side=TOP,expand=YES,fill=BOTH)
	
	Button(root,text='huatu',command=drawpic).pack(side=BOTTOM,expand=YES,fill=BOTH)

	root.mainloop()
		