import math 
import random


class Player :
    def __init__(self , letter) :
        
        #letter is X or O
        self.letter = letter

    def GetMove(self , game) :
        pass


class RandomComputerPlayer (Player) :
    def __init__(self, letter):
        super().__init__(letter)

    def GetMove(self, game):

        #get a random valid spot for next move
        square = random.choice(game.AvailbleMoves())
        
        return square
    



class HumanPlayer (Player) : 
    def __init__(self, letter):
        super().__init__(letter)

    def GetMove(self, game):
        ValidSquare = False
        val = None

        while not ValidSquare :
            square = input(self.letter + '\'s turn.Input move (0_8): ')
      
            #to check that is value valid or not by try and except
            try :
                val = int(square)

                if val not in game.AvailbleMoves() :
                    raise ValueError
                else : 
                    ValidSquare =True
            except ValueError:
                print("Invalid square , Try again")            


        return val
