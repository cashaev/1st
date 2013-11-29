from Tkinter import *
from environment import Environment
import Tkinter

x = [0]* ALL_DOTS
y = [0] * ALL_DOTS
DELAY = 100
DOT_SIZE = 10
RAND_POS = 27

class App():
    environment = Environment(10,10)
    height = 500
    width = 500
    ALL_DOTS = len(environment) * len(environment) / (DOT_SIZE * DOT_SIZE)
    def __init__ (self,top):
        print "initialized"
        self.top = top
        self.create_lines()
        self.create_menu()
        
        self.initGame()

        print "packed"
    
    def create_lines(self):
        
        C = Tkinter.Canvas(self.top, height=self.height,width=self.width,cursor="dot")
        print self.height, self.width
        for i in range(0,len(self.environment.surface)):
            coord =0,(i)*self.height/len(self.environment.surface),self.width,(i)*self.height/len(self.environment.surface)

            C.create_line(coord)
            coord =(i)*self.width/len(self.environment.surface),0,(i)*self.width/len(self.environment.surface),self.height

            C.create_line(coord)
        C.pack()

    def create_menu(self):

        menubar = Menu (self.top)
        self.top.config(menu=menubar)

        filemenu = Menu(menubar)
        filemenu.add_command(label="Quit",command=self.onQuit())
        menubar.add_cascade(label="File",menu=filemenu)

        
    def mainloop(self):
        self.top.mainloop()

    def onQuit(self):
        import sys
        print "quitting"
        self.top.quit()

    def initgame(self):
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.inGame = True
        self.dots = 3

        self.apple_x = 100
        self.apple_y = 190

        for i in range(self.dots):
            x[i] = 50 - i*10
            y[i] = 50

        try:
            self.idot = Image.open("dot.png")
            self.dot = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open("head.png")
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.Open("apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError, e:
            print e
            sys.exit(1)

        self.focus_get()

        self.createObjects()
        self.locateApple()
        self.bind_all("<Key>",self,onKeyPressed)
        self.after(DELAY,self,onTimer)

    def createObjects(self):
        self.create_image(self.apple_x,self,apple_y,image=self.apple,anchor=NW,tag = "apple")
        self.create_image(50,50,image = self.head, anchor = NW, tag = "head")
        self.create_image(30,50,image = self.dot, anchor = NW, tag = "dot")
        self.create_image(40,50,image = self.dot, anchor = NW, tag = "dot")

    def checkApple(self):
    
        apple = self.find_withtag("apple")
        head = self.find_withtag("head")
    
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
    
        for ovr in overlap:
        
            if apple[0] == ovr:
            
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
                self.locateApple()