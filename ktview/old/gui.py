from Tkinter import *
from graph import Graph

master = Tk()
frame = Frame()
g = Graph(frame)
g.update_data([1,2,3,4,5],[5,6,1,3,8])
mainloop()
