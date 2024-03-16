import random

def Guess(x) : 
   
    RandomNumber = random.randint(1 , x)    
    guess = 0
    
    while guess != RandomNumber :
        guess = int(input(f"Guess a number between 1 and {x}: ") )
        if guess<RandomNumber :
            print("Guess a bigger number.")
        elif guess>RandomNumber : 
            print ("Guess a smaller number.")
    
    print(f"You guessed the number {RandomNumber}!")

Guess(10)