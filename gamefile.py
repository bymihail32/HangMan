import random
import time

print('Welcome to the HangMan Games!')
time.sleep(1)
name = input("What is your name? ")
time.sleep(1)
print("Good Luck ! ", name)
time.sleep(1)

countries = ['Romania', 'Slovenia', 'Italia', 'Franta', 'Spania', 'Austria', 'Germania', 'Moldova',
                 'Polonia', 'Anglia']
word = random.choice(countries)
guesses = ''
turns = 3

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print (char,end="")
        else:
            print ("_",end=""),
            failed += 1
    if failed == 0:
        print ("\nYou won! The word was: " + word)
        break
    guess = input("\nGuess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nWrong")
        print("\nYou have", + turns, 'more guesses')
        if turns == 0:
            print ("\nYou lost. The word was: " + word)

