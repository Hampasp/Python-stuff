import random

number = random.randint(1,10)

player_name = input("Hello! What is your name? ")

print('Okay! '+ player_name + ' What number am I guessing?')

number_of_guesses = 0

while number_of_guesses < 5: 
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("your guess is too low!")
    if guess > number:
        print("your guess is too high!")
    if guess == number:
        break
if guess == number:
    print("You guessed right after " + str(number_of_guesses) + " attempts!")
else:
    print("You didn't guess right! The number was " + str(number))