class Environment:
    surface=[]
    def __init__(self,width,length):
        self.width = width
        self.length = length
        
        for i in range(0,self.length):
            self.surface.append([0]*width)
