import random
import string

Words = ["elephant", "computer", "rainbow", "sunshine", "butterfly", "watermelon", "adventure", "baseball", "happiness", "chocolate", "pizza", "unicorn", "zombie", "fireworks", "carnival", "basketball", "sunflower", "pineapple", "waterfall", "giraffe", "octopus", "raincoat", "penguin", "dragonfly", "firecracker", "festival", "snowflake", "mermaid", "volcano", "cupcake", "bicycle", "butterfly", "tiger", "dolphin", "popcorn", "sunglasses", "sunscreen", "umbrella", "jellyfish", "caterpillar", "diamond", "parrot", "guitar", "moonlight", "camouflage", "carousel", "chameleon", "coffee", "daisy", "disco", "eclipse", "fireplace", "fountain", "fragrance", "galaxy", "harmony", "hurricane", "illusion", "jasmine", "kangaroo", "kiwi", "lagoon", "liberty", "lobster", "magician", "marshmallow", "mystery", "nebula", "orchid", "oxygen", "piano", "pyramid", "quartz", "raccoon", "rainforest", "sandcastle", "sapphire", "starlight", "tornado", "treasure", "twilight", "umbrella", "valentine", "whale", "xylitol", "yellow", "zeppelin"]



def Hangman() : 
    Word = random.choice(Words).upper() 

    WordLetter = set(Word) #letters in the word

    Alphabet = set(string.ascii_uppercase) 
    
    UsedLetters = set() #what the user has guessed
    
    while len(WordLetter) > 0 :
        
        print("You have used this letters: " ,' '.join(UsedLetters)) # tell the user which letters are used

        WordList = [letter if letter in UsedLetters else '-' for letter in Word]

        UserLetters = input("Guess a letter: ").upper() #getting user input

        if UserLetters in Alphabet - UsedLetters : 
            UsedLetters.add(UserLetters)

            if UserLetters in WordLetter :
                WordLetter.remove(UserLetters) 

        elif UserLetters in UsedLetters : 
            print("You have already used this character , please try again: ")

        else : 
            print("invalid character , please enter a valid one: ")    


        print("Current word: " , ' '.join(WordList))

    print(f"the word is {Word}")    



Hangman()    

