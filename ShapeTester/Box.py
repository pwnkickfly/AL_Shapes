class Box:
    def __init__(self,l,w,h):
        self.l = l
        self.w = w
        self.h = h
    def getVolume(self):
        return self.l*self.w*self.h
    def getSurfArea(self):
        2*(self.l*self.w + self.h*self.l + self.h*self.w)
