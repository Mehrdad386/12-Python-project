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
                    ValidSquare = True
            except ValueError:
                print("Invalid square , Try again")            


        return val


class GeniusComputerPlayer(Player) :
    
    def __init__(self , letter):
        super().__init__(letter)

    def    GetMove(self , game) :
        if len(game.AvailbleMoves()) == 9 :
            square = random.choice(game.AvailbleMoves())
        else :
            #get the square based on minimax algorithm
            square = self.Minimax(game , self.letter)['position']
        return square

    
    def Minimax(self , state , player) : 
        MaxPlayer = self.letter #yourself
        OtherPlayer = 'O' if player == 'X' else 'X'

        #first we check that the previous move is a winner
        if state.CurrentWinner == OtherPlayer :
            #we should return position and score   

            return {'position' : None ,
                    'score' : 1 * (state.NumEmptySquare()+1) if OtherPlayer == MaxPlayer else -1 * (state.NumEmptySquare() +1)
                    } 
        elif not state.EmptySquare() : 
            return {'positon' : None , 
                    'score' : 0 }
        
        if player == MaxPlayer :
            best = {'position' : None ,
                    'score' : - math.inf} #each score should maximize
        
        else :
            best = {'position' : None ,
                    'score' :  math.inf} # each score should be minimize

        for PossibleMove in state.AvailbleMoves() :
            
            #step1 : make a move
            state.MakeMove(PossibleMove , player)

            #step2 : using minimax
            SimScore = self.Minimax(state , OtherPlayer)

            #step 3 : undo the move
            state.board[PossibleMove] = ' '
            state.CurrentWinner = None
            SimScore['position'] = PossibleMove

            #step4 : update dictionaries
            if player == MaxPlayer : 
                if SimScore['score'] > best['score'] : 
                    best = SimScore #replace best

                else : 
                    if SimScore['score'] < best['score'] :
                        best = SimScore #replace best
        return best   

