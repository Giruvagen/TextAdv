#starts the games
import Character
import Moves
class starter(Character, Moves):
        def startGame(self):
          self.char = input("What is your name? ")
          print(self.char)
          player.startRoll()

starter.startGame()