#starts the games
from Character import Character
from Moves import motion
class starter(motion, Character):
        def __init__(self, name):
          self.name = name
          self.st = 0
          self.defe = 0
          self.spd = 0
          self.char = ""
        def startGame(self):
          self.startGame()
char = input("What is your name? ")
player = starter(char)          
player.startGame()


