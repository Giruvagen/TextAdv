#Init character with initial values
import random
import time
class Character:
    def __init__(self,name,st,defe,spd):
      self.name = name
      self.st = st
      self.defe = defe
      self.spd = spd
    def startGame(self):
        print("Let the games begin!")
        self.startmove(self.name)
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
