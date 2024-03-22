import time
from Player import HumanPlayer , RandomComputerPlayer , GeniusComputerPlayer



class TicTacToe :
    def __init__ (self) :
        self.board = [' ' for _ in range(9)] # we use a single list to rep 3x3 board
        self.CurrentWinner = None #keep track of winner

    def PrintBoard (self) :
        #to make the rows with empty space 
        for row in [self.board[i*3 : (i+1) * 3] for i in range(3)] :
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def PrintBoardNums() :
        #print numbers in spaces
        NumberBoard = [[str(i) for i in range (j*3 , (j+1) * 3)] for j in range(3)]

        for row in NumberBoard :
            print('| ' + ' | '.join(row) + ' |')

    def AvailbleMoves(self) :
        # return [i for i , spot in enumerate(self.board) if spot == ' ']
        moves = []
        
        #enumerate = it will return the index with it's value as a list of Tupples for example [('0' ,'X') , ('1' , ' ') , ...]
        for (i,spot) in enumerate(self.board) :
            if spot == ' ' :
                moves.append(i)

        return moves         
            

    def EmptySquare(self) :

        return ' ' in self.board # it returns a bool value
    

    def NumEmptySquare (self) :
        
        # empties = 0 
        # for empty in self.board :
        #     if empty == ' ' :
        #         empties += 1
        
        
        # return empties
        
        #return len(self.AvailbleMoves())
        return self.board.count(' ')



    



    def MakeMove (self , square , letter) :
        #we return bool to check is this square availble or not
        if self.board[square] == ' ' :
            
            self.board [square] = letter

            if self.Winner(square , letter) :
                self.CurrentWinner = letter
            
            return True

        return False




    def Winner (self , square , letter) :
        

        #check the rows
        RowInd = square //3

        row = self.board[RowInd*3 : (RowInd +1) *3]

        #check rows
        if all( spot == letter for spot in row) :
            return True
        

        #check  the columns
        ColInd = square%3 
        column = [self.board[ColInd + i*3] for i in range(3)]

        if all( spot == letter for spot in column) :
            return True
        
        #check diagnols
        if square%2 == 0 :
            diagnols1 =[self.board[i] for i in  [0,4,8]] #left to right
            if all ([spot == letter  for spot in diagnols1]) :
                return True
            
            diagnols2 =[self.board[i] for i in  [2,4,6]] # right to left
            if all ([spot == letter  for spot in diagnols2]) :
                return True


        return False







def Play(Game , Xplayer , Oplayer , PrintGame = True) :
#return winner or None

    if PrintGame : 

        Game.PrintBoardNums()

    letter = 'X' #starting letter
    
    #keep looping untill there is no empty square and for winning or being tie we just break it
    while Game.EmptySquare() :

        # get the move from appropriate player
        if letter == 'O' :
            square = Oplayer.GetMove(Game)

        elif letter == 'X' :
            square = Xplayer.GetMove(Game)


        if Game.MakeMove( square , letter) :
            if PrintGame :

                print(letter + f" make a move to square {square}")
                Game.PrintBoard()
                print('') # to have an empty line


        if Game.CurrentWinner :
            if PrintGame :
                print(letter + " wins!")

            return letter
        

        if letter == 'X' :
            letter = 'O'
        elif letter == 'O' :
            letter = 'X'


        time.sleep(0.5) # short sleep to read texts easier


    if PrintGame :
        print("It\'s a tie!")






if __name__  == '__main__' :
    Xplayer = HumanPlayer('X')
    Oplayer = GeniusComputerPlayer('O')
    t = TicTacToe()

Play(t , Xplayer , Oplayer , PrintGame= True)