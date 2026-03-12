import random
print("Welcome to the Hangman game")
print("Try to guess the animal name")
Animals = ["elephant", "giraffe", "lion", "tiger", "koala", "whale", "sloth", "ox", "fox", "deer", "gazelle"]
Word = random.choice(Animals)
Guessed_Letter = set()
displayed_word = ''.join([letter if letter in Guessed_Letter else "_" for letter in Word])
print(displayed_word)
Hangman_Stages = [
    """
       ------
       |    |
       |    
       |    
       |    
       |    
    --------
    """,
     """
       ------
       |    |
       |    O
       |    
       |    
       |    
    --------
    """, 
    """
       ------
       |    |
       |    O
       |    |
       |    
       |    
    --------
    """,
      """
       ------
       |    |
       |    O
       |   /| 
       |    
       |    
    --------
    """,
      """
       ------
       |    |
       |    O
       |   /|\\
       |    
       |    
    --------
    """, 
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |    
    --------
    """, """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |    
    --------
    """,
]
Atempt = 6
while Atempt >= 1:
    print(Hangman_Stages[6 - Atempt])
    Guess = input("Guess a letter ")
    if len(Guess) != 1 or not Guess.isalpha():
        print("Error")
        continue
    if Guess in Guessed_Letter:
        print("You have already guessed this letter")
        continue
    Guessed_Letter.add(Guess)
    if Guess in Word:
        print("Correct, nice guess")
    else:
        print("Incorrect, you lost an attempt")
        Atempt = Atempt - 1

    print("Guessed letter", Guessed_Letter)
    displayed_word = ''.join([letter if letter in Guessed_Letter else "_" for letter in Word])

    print("Displayed word", displayed_word)

    print("You have", Atempt, "Atempts left")

    if displayed_word == Word:
        print("Congrats you win")
        break

if Atempt == 0:
    print(Hangman_Stages[-1])
    print("Game over, better luck next time")
    print("The word was", Word)
    
    