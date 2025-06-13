import random

# print(help(random))
# number = random.randint(1, 6)           #Generate a random number from 1 to 6
# print(number)

# low = 1
# high = 100
# number2 = random.randint(low, high)
# print(number2)

# num = random.random()                   #Genrate between 0.0 and 0.9999 (include 0.0 but exclude 1.0)

# options = ("Rock", "Paper", "Scissor")
# option = random.choice(options)           #Generate one element among the three
# print(option)

# cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "K", "Q", "J"]
# random.shuffle(cards)                     #Shuffe the whole list
# print(cards)    

#Python number guessing game

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses =  0
is_running = True

print("Python Number guessing game!")

while is_running:
    guess = input(f"Select a number between {lowest_num} & {highest_num}: " + '\n')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range!")
            guess = input(f"Select a number between {lowest_num} & {highest_num}: " + '\n')
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else :
            print(f"Correct! The number was {answer}.")
            print(f"Your number of attempts: {guesses}")
            is_running = False
    else :
        print("Invalid input!")
        guess = input(f"Select a number between {lowest_num} & {highest_num}: " + '\n')
        
        print("Invalid input!")
        print("Game restarted!")
        print("Insert your guess 2 times! The second guess will be the new game!")

# OR 
# answer = random.randint(0,101)
# print("Guess a random number from 1-100") 