#defines movement
import random
from content import mapdesc
class motion(object):

    def __init__(self, char):
      self.char = char
    def move(self, direction):
        if self.direction == "north":
            self.starty += 1
            print(mapdesc[(self.startx,self.starty)])
        elif self.direction == "south":
            self.starty -= 1
            print(mapdesc[(self.startx,self.starty)])
        elif self.direction ==  "east":
            self.startx += 1
            print(mapdesc[(self.startx,self.starty)])
        elif self.direction == "west":
            self.startx -= 1
            print(mapdesc[(self.startx,self.starty)])
        self.direction = input("Choose your direction of travel: ")
        self.move(self.direction)
    def startmove(self):
      self.startx = random.randint(0,2)
      self.starty = random.randint(0,2)
      print("Here begins your adventure, {:s}, at spot {:d},{:d}".format(self.char,self.startx,self.starty))
      print(mapdesc[(self.startx,self.starty)])
      self.direction = input("Choose your direction of travel: ")
      self.move(self.direction)
