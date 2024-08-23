from random import *

number: int = randint(1,10)

guess = 0

while guess != number:
    guess = int(input("Arvaa numero 1-10 välillä: "))
    if guess == number:
        print("Oikein")
        break
    elif guess < number:
        print("Liian pieni arvaus")
    elif guess > number:
        print("Liian suuri arvaus")