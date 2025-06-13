import random

lowest_num = 1
highest_num = 101
is_running = True
guesses = 0

answer = random.randint(lowest_num, highest_num)

print("Python number guessing game.")

while is_running:
    guess = input("Guess a random number between 1 & 100: \n")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1 
        
        if guess < 1 or guess > 100:
            print("Invalid value! Value must be between 1 and 101!")

        elif guess == answer:
           print("Correct")
           print(f"The answer was {answer}!")
           print(f"It took you {guesses} attempts.")
           is_running == False
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")

    else:
        print("No! Enter a number between 1 and 101.")

    
           
        
    
    