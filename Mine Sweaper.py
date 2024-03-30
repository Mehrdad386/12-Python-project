import random
import re

class Board :
    def __init__(self , size , BombNum) :
        
        #keeping track of parameters
        self.size = size
        self.BombNum = BombNum

        #helper functions
        self.board = self.MakeNewBoard()
        self.AssignValuesToBoard()

        #we will save (row,col) tuple into this
        self.dug = set()


    def MakeNewBoard (self) :
        
        board = [[None for i in range(self.size )] for j in range(self.size)]

        PlantedBomb = 0

        while PlantedBomb < self.BombNum  :
            loc = random.randint(0 , (self.size **2 - 1))

            row = loc// self.size

            col = loc % self.size

            if board[row][col] == '*' :
                #it means we have already planted a bomb in this index
                continue
            

            board[row][col] = '*'  #plant the bomb
            PlantedBomb += 1


        return board






    def AssignValuesToBoard (self)  :
        #assign a number between 0_8 to empty spaces to show number of bombs around that space
        for r in range(self.size) :
            for c in range (self.size) :
                if self.board[r][c] == '*' :
                    continue
                
                self.board[r][c] = self.GetNumNeighborBombs( r , c)


    def GetNumNeighborBombs (self , row , col) :

        NeighborBombNum = 0 

        for r in range(max (0 , row -1) , min(self.size - 1 , (row + 1)+1)) :
            for c in range (max(0, col - 1) ,min(self.size - 1 , (col+1) + 1)) :
                if r == row and col == c :
                    #our orginal location , must be skiped
                    continue
                
                if self.board[r][c] == '*' :
                    NeighborBombNum += 1

        return NeighborBombNum
    

    def Dig (self , row , col) :
        #to dig at location 
        #return True if successful , False if bomb dug

        #hit a bomb -> game over
        #hit a location with neighboring bomb -> finish dig 
        #dig at location with no neighboring bomb  -> recursively dig neighbors

        self.dug.add((row,col)) #keep track that we dug here

        if self.board[row][col] == '*' :
            return False
        elif self.board[row][col] > 0 :
            return True
        

        
        for r in range(max (0 , row -1) , min(self.size - 1 , (row + 1)+1)) :
            for c in range (max(0, col - 1) ,min(self.size - 1 , (col+1) + 1)) :
                if (r,c) in self.dug :
                    continue
                else :
                    self.Dig(r,c)

        
        return True


    def __str__ (self) :
        
        VisibleBoard = [[None for i in range(self.size)] for j in range (self.size)]

        for row in range(self.size) :
            for col in range(self.size) :
                if (row,col) in self.dug :
                    VisibleBoard[row][col] = str(self.board[row][col])

                else : 
                    VisibleBoard[row][col] = ' '

       #put this together in  a string 
        StringRep = ''
       
        #get max columns widths for printing
        widths = []
        for idx in range(self.size) :
            columns = map(lambda x : x[idx] , VisibleBoard)
            widths.append(len(max(columns , key= len)))


        #print Csv string
        indices = [i for i in range(self.size)]
        IndicesRow = '  '
        cells = []

        for idx , col in enumerate(indices) :
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))

        IndicesRow += '  '.join(cells)
        IndicesRow += '  \n'

        for i in range(len(VisibleBoard)) :
            row = VisibleBoard[i]

            StringRep += f'{i} |'

            cells = []

            for idx , col in enumerate(row) :
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))

            StringRep += ' |'.join(cells)
            StringRep += '  \n'

        StrLen = int (len(StringRep) / self.size)
        StringRep = IndicesRow + '-' *StrLen + '\n' + StringRep + '-'*StrLen

        return StringRep





#play the game
def Play(BoardSize = 10 , BombNum = 10) :
    #step 1: create the board and bombs
    board = Board(BoardSize , BombNum)


    #step 2: print board and ask user for where he/she wants to dig
    #step 3a: if location is a bomb -> show game over
    #step 3b: if location is not a bomb  -> continue untill each square at least next to a bomb
    #step 4: repeat step 2 , 3 untill there is no empty space to dig -> Victory
    
    safe = True

    while len(board.dug) < (board.size **2) - BombNum :
        
        print(board)
        
        UserInput = re.split(',(\\s)*',input("where would you like to dig? input as row,col: "))

        row,col = int(UserInput[0]) , int(UserInput[-1])
        if row < 0 or row >= board.size or col<0 or col >=board.size :
            print("Invalid location , Try again.")
            continue

        
        safe = board.Dig(row , col)
        
        if not safe : 
            break #game over

    if safe :
        print("You won")
    else : 
        print("You lost")

        board.dug = [(r,c) for r in range(board.size) for c in range(board.size)]
        print(board)




if __name__ == "__main__" :
    Play()
     