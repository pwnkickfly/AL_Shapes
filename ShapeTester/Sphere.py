import math
class Sphere:
    def __init__(self,r):
        self.r = r
    def getVolume(self):
        return 4/3*math.pi*self.r**3
    def getSurfArea(self):
        return 4*math.pi*self.r**2
