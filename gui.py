import Tkinter as Tkinter
from Tkinter import *
class App(Frame):
    height = 0
    environment = []
    width = 0
    def __init__ (self,environment,height,width,master=None):
        #Tkinter.Frame.__init__(self,master=None)
        self.environment = environment
        self.height = height
        self.width = width
        print "initialized"
        self.create_lines(master)
    
    def create_lines(self,master):
        
        C = Tkinter.Canvas(master, height=self.height,width=self.width,cursor="dot")
        for i in range(0,len(self.environment.surface)):
            coord =0,(i)*self.height/len(self.environment.surface),self.width,(i)*self.height/len(self.environment.surface)
            C.create_line(coord)
            coord =(i)*self.width/len(self.environment.surface),0,(i)*self.width/len(self.environment.surface),self.height
            C.create_line(coord)
        master.pack()

