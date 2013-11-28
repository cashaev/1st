from gui import *
from environment import Environment

e = Environment(10,10)
myapp = App(e,500,500)
#myapp.create_lines(e,500,500)
myapp.mainloop()
