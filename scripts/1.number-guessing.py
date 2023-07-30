# pylint: disable=trailing-whitespace
""" 
    importing random module 
"""
import random 


number = random.randint(1, 9)
number_of_guesses = 0
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    number_of_guesses += 1
    if guess != number:
      print('Topolmadingiz yana bir bor urinib ko\'ring number')
    elif guess == number:
      break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")
