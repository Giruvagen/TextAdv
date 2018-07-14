#defines movement
import random
from content import mapdesc
from content import monsters
class motion(object):
    def __init__(self, char):
      self.char = char
    def gameOver(self):
        print("You died! Game over man!")
        self.startGame()
    def battle(self):
        print("A monster appears!")
        self.monster = random.choice(list(monsters.items()))
        print("It's a wild {}!".format(self.monster[0]))
        fightChoice = input("What will you do, run or fight? ")
        if fightChoice == "fight":
            yourAttack = self.st + random.randint(1,4)
            monsterAttack = self.monster[1] + random.randint(1,4)
            if yourAttack > monsterAttack:
                print("You won! The monster is vanquished!")
            elif monsterAttack > yourAttack:
                print("You lost!")
                self.gameOver()
        elif fightChoice == "run":
            print("You ran away, such cowardice!")
        else:
            print("You have to fight or run!")
            self.battle()
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
