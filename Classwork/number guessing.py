import random

x = random.randrange(1,11)

for attempts in range(5, 0, -1):
    print(f"You have {attempts} attempts.")
    guess = input("Guess between 1 to 10: \n")
    guess = int(guess)

    if guess == x:
        print(f"You won! The number was {x}.")
        print(f"It took you", 6 - attempts , "attempt/s.")
        break
    elif guess > x:
        print("Too high!")
    elif guess < x:
        print("Too low!")
    else:
        print(f"You lost! You have {attempts} lefts.")
        continue
