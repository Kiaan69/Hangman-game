🪢 Hangman Game (Python)

A simple command-line Hangman game written in Python.
The player tries to guess the name of an animal one letter at a time before the hangman drawing is completed.

This project is a beginner-friendly Python program that demonstrates the use of:

loops

lists

sets

conditional statements

user input

random word selection

🎮 How the Game Works

The program randomly selects an animal name from a predefined list.

The word is hidden using underscores (_).

The player guesses one letter at a time.

If the letter is correct, it appears in the word.

If the letter is incorrect, the player loses an attempt and the hangman drawing progresses.

The player has 6 attempts before the game ends.

You win if you reveal the entire word before running out of attempts.

🐾 Animal Word List

The game currently selects from the following animals:

elephant

giraffe

lion

tiger

koala

whale

sloth

ox

fox

deer

gazelle

🖥 Example Gameplay
Welcome to the Hangman game
Try to guess the animal name

_ _ _ _ _

Guess a letter: a
Correct, nice guess

Displayed word: _ a _ a _
You have 6 attempts left
⚙️ Requirements

Python 3.x

No external libraries are required. The game only uses Python's built-in modules.

▶️ How to Run the Game

Clone this repository

git clone https://github.com/yourusername/hangman-python.git

Navigate into the project folder

cd hangman-python

Run the program

python hangman.py
📚 What I Learned

While building this project, I practiced:

Using the random module

Working with sets to store guessed letters

Creating loops to control game flow

Displaying game states using ASCII art

Validating user input
