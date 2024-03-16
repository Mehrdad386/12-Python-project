import random


def Play() :
    User = input("'r' for Rock , 'p' for Paper , 's' for for Scissors choose one of them? ").lower()
    Computer = random.choice(['r' , 'p' , 's'])


    if User == Computer : 
        return "Tie"
    
    if IsWin(User , Computer ) :
        return "You Won!"
    
    return "You lost!"



def IsWin(player , opponent) : 

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') :
        return True 


print(Play())