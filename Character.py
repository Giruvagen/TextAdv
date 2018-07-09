#Init character with initial values
import random
class Character(object):
    def __init__(self,name):
      self.name = name
    def startroll(self):
        print("Please select your intial statistics. Please note you may not set a single item to higher than 4 and the total of all 3 must be less than 10")
        atts = []
        self.st = int(input("What is your strength?"))
        atts.append(self.st)
        self.defe = int(input("What is your defence?"))
        atts.append(self.defe)
        self.spd = int(input("What is your speed?"))
        atts.append(self.spd)
        if atts[0] >= 5 or atts[1] >= 5 or atts[2] >= 5:
          print("The number you entered, is too damn high!")
        elif sum(atts) > 10:
          print("The total you entered, is too damn high!")
        else:
          print("Thank you.")
          self.st = atts[0] + random.randint(0,5)
          self.defe = atts[1] + random.randint(0,5)
          self.spd = atts[2] + random.randint(0,5)
          print("Your strength is {:d}".format(self.st))
          print("Your defence is {:d}".format(self.defe))
          print("Your speed is {:d}".format(self.spd))
