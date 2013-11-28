from gui import *
from environment import Environment
from Tkinter import *


e = Environment(10,10)
root = Tk("App")
myapp = App(e,500,500,master=root)
#myapp.create_lines(e,500,500)
myapp.mainloop()
