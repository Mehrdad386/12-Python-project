import random


def ComputerGuess(x) :

    print("Imagine an number beetween 1 to 10")

    Low = 1
    High = x
    Feedback = ""

    while Feedback != "c"  :

        if  Low != High :
           Guess = random.randint(Low , High)
        else : 
            Guess = Low  #could also be high

        Feedback = input(f"Is {Guess} too high (H), too low (L), or correct (C)?? ").lower()

        if Feedback == "h" :
            High = Guess - 1            
        elif Feedback == "l" :
            Low = Guess + 1

    print(f"The computer guessed the number {Guess} correctly!")        



ComputerGuess(10)