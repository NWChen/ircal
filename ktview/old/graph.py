import matplotlib
import Tkinter as tk

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class Graph(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.graph = self.figure.add_subplot(1, 1, 1)
        #canvas = FigureCanvasTkAgg(self.figure, self)
        #canvas.show()
        #canvas.get_tk_widget().pack()

    def update_data(self, x, y):
        self.graph.plot(x, y)
        canvas = FigureCanvasTkAgg(self.figure, self)
        canvas.show()
        canvas.get_tk_widget().pack()
