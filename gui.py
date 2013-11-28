import Tkinter as Tkinter


class App(Tkinter.Frame):

    def __init__ (self,environment,height,width):
        
        self = Tkinter.tk()
        #Tkinter.Frame.__init__(self,master=None)
        #self.create_lines(environment,height,width)
    
    def create_lines(self,environment,height,width):
        
        C = Tkinter.Canvas(self, height=height,width=width,cursor="dot")
        for i in range(0,len(environment.surface)):
            coord =0,(i)*height/len(environment.surface),width,(i)*height/len(environment.surface)
            C.create_line(coord)
            coord =(i)*width/len(environment.surface),0,(i)*width/len(environment.surface),height
            C.create_line(coord)
        self.pack()

