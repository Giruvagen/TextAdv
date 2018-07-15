#class for generating a random map
import random
from content import maptypelist
import math
import collections
class randMap(object):
    def __init__(self):
        self.seed = random.randint(0,2048)
        self.mapx = random.randint(32,64)
        self.mapy = random.randint(32,64)
        self.centrex = int(self.mapx/2)
        self.centrey = int(self.mapy/2)
        self.centre = (self.centrex,self.centrey)
    def starter(self):
        self.mapxrange = list(range(self.mapx))
        self.mapyrange = list(range(self.mapy))
        self.maptup = []
        self.mapkeytotal = self.mapxrange * self.mapyrange
        for x in self.mapxrange:
            for y in self.mapyrange:
                self.maptup.append([x,y,""])
        self.mapcomplete = []
        self.mapvalues = []
        for i in self.maptup:
          i[2] = random.choice(maptypelist)
        self.mapdict = collections.OrderedDict()
        count = 0
        for i in self.maptup:
            self.mapdict[count] = i
            count += 1
