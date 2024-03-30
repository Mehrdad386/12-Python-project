def FindNextEmpty(puzzle):
   #find the next row,col on the puzzle that is not filled yet -> rep with -1
    #return (row,col) tupple or (None,None) if there is none
    
    for r in range(9) :
        for c in range(9) :
            if puzzle[r][c] == -1 :
                return r,c

    return None,None # if there is no empty space on the puzzle



def IsValid(puzzle , guess , row , col) : 
    #return True if it is valid and False if it is not

    #check the row
    RowVals = puzzle[row]
    if guess in RowVals :
        return False

    #check the col
    ColVal = [puzzle[i][col] for i in range(9)]
    if guess in ColVal :
        return False
    
    #check the square 3x3
    RowStart = row//3
    ColStart = col//3

    for r in range(RowStart , RowStart +3) :
        for c in range(ColStart , ColStart + 3) :
            if puzzle[r][c] == guess :
                return False
            

    return True



def SolveSudoku(puzzle) :
    #solve Sudoku using backtracking technic
    #our pzzle is a list of lists where each inner list is a row

    #step 1: choose somewhere on the puzzle to make a guess
    row , col = FindNextEmpty(puzzle)

    #step 1.1 : if there is no empty space -> we're done
    if row is None :
        return True
    
    #step 2: if there is an empty place  then make a guess between 1 and 9
    for guess in range (1,10) :
        #step 3: check if it is a valid guess
        if IsValid(puzzle , guess , row , col) :
            #step 3.1 : if it's valid -> place it on puzzle
            puzzle[row][col] = guess
            #step 4: recursively call our fuction
            if SolveSudoku(puzzle) :
                return True
        
        #step 5: if it's not valid we need to backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess

    #if all numbers didn't work -> this is on solveable
    return False



if __name__ == '__main__' :
    ExamplePuzzle = [
        [3,9,-1 ,   -1,5,-1,   -1,-1,-1 ],
        [-1,-1,-1,   2,-1,-1,   -1,-1,5 ],
        [-1,-1,-1,   7,1,9,     -1,8,-1 ],

        [-1,5,-1,   -1,6,8,    -1,-1,-1 ],
        [2,-1,6 ,   -1,-1,3,   -1,-1,-1 ],
        [-1,-1,-1,   -1,-1,-1,  -1,-1,4 ],

        [5,-1,-1,   -1,-1,-1,    -1,-1,-1 ],
        [6,7,-1 ,   -1,-1,5,     -1,4,-1  ],
        [1,-1,9,   -1,-1,-1,    2,-1,-1  ]
    ]
    print(SolveSudoku(ExamplePuzzle))
    print(ExamplePuzzle)