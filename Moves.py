#defines movement
import random
from content import mapdesc
from content import monsters
class motion(object):

    def __init__(self, char):
      self.char = char
    def battle(self):
        print("A monster appears!")
        self.monster = random.choice(list(monsters.items()))
        print("It's a wild {:s}!".format(self.monster))
        self.move(self.direction)
    def move(self, direction):
        if self.direction == "north":
            self.starty += 1
            if self.starty > 2:
                self.starty = 0
                print(mapdesc[(self.startx,self.starty)])
            else:
              print(mapdesc[(self.startx,self.starty)])
              self.battlechance = random.randint(0,8)
              if self.battlechance == 1:
                self.battle()
        elif self.direction == "south":
            self.starty -= 1
            if self.starty < 0:
                self.starty = 2
                print(mapdesc[(self.startx,self.starty)])
            else:
              print(mapdesc[(self.startx,self.starty)])
              self.battlechance = random.randint(0,8)
              if self.battlechance == 1:
                self.battle()
        elif self.direction ==  "east":
            self.startx += 1
            if self.startx > 2:
                self.startx = 0
                print(mapdesc[(self.startx,self.starty)])
            else:
              print(mapdesc[(self.startx,self.starty)])
              self.battlechance = random.randint(0,8)
              if self.battlechance == 1:
                self.battle()
        elif self.direction == "west":
            self.startx -= 1
            if self.startx < 0:
                self.startx = 2
                print(mapdesc[(self.startx,self.starty)])
            else:
              print(mapdesc[(self.startx,self.starty)])
              self.battlechance = random.randint(0,8)
              if self.battlechance == 1:
                self.battle()
        else:
            print("Please choose a valid direction: north, south, east or west!")
        self.direction = input("Choose your direction of travel: ")
        self.move(self.direction)
    def startmove(self):
      self.startx = random.randint(0,2)
      self.starty = random.randint(0,2)
      print("Here begins your adventure, {:s}, at spot {:d},{:d}".format(self.char,self.startx,self.starty))
      print(mapdesc[(self.startx,self.starty)])
      self.direction = input("Choose your direction of travel: ")
      self.move(self.direction)
