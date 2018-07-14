#Init character with initial values
import random
import time
from content import mapdesc
from content import monsters
class starter(object):
        def __init__(self, name):
          self.name = name
          self.st = 0
          self.defe = 0
          self.spd = 0
          self.char = ""
        def startGame(self):
          print("Let the games begin!")
          self.startmove()
        def startRoll(self):
          print("Please select your intial statistics. Please note you may not set a single item to higher than 4 and the total of all 3 must be less than 10")
          atts = []
          self.st = int(input("What is your strength? "))
          atts.append(self.st)
          time.sleep(2)
          if atts[0] >= 5:
            print("The number you entered, is too damn high!")
            time.sleep(3)
          self.defe = int(input("What is your defence? "))
          atts.append(self.defe)
          time.sleep(2)
          if atts[1] >= 5:
            print("The number you entered, is too damn high!")
            time.sleep(3)
          self.spd = int(input("What is your speed? "))
          atts.append(self.spd)
          time.sleep(2)
          if atts[2] >= 5:
            print("The number you entered, is too damn high!")
            time.sleep(3)
          if sum(atts) > 10:
            print("The total you entered, is too damn high! Try Again!")
            time.sleep(3)
            self.startRoll()
          else:
            print("Thank you.")
            time.sleep(5)
            self.st = atts[0] + random.randint(0,5)
            self.defe = atts[1] + random.randint(0,5)
            self.spd = atts[2] + random.randint(0,5)
            print("Your strength is {:d}".format(self.st))
            time.sleep(1)
            print("Your defence is {:d}".format(self.defe))
            time.sleep(1)
            print("Your speed is {:d}".format(self.spd))
            time.sleep(1)
            self.startGame()
#defines movement
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
            print("You strike for {} damage!".format(yourAttack))
            monsterAttack = self.monster[1] + random.randint(1,7)
            print("The monster strikes for {} damage!".format(monsterAttack))
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
char = input("What is your name? ")
player = starter(char)
player.startRoll()
