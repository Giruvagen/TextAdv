#starts the games
from Character import Character
from Moves import motion
class starter(Character, motion):
        def __init__(self, name, st, defe, spd, char):
          self.name = name
          self.st = st
          self.defe = defe
          self.spd = spd
          self.char = char
        def startGame(self):
          self.startRoll()
char = input("What is your name? ")
player = starter(char,0,0,0,char)          
player.startGame()


