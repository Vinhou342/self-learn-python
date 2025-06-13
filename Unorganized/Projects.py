import math
import time

#print("This is a cicle circumference calculator")
#radius = float(input("Enter the radius: "))
#circumference = 2 * math.pi * radius
#Area_of_surface = math.pi * pow(radius, 2)
#print("The circumference is " + f"{circumference}")
#print("The area of circle is " + f"{Area_of_surface}")

#print(Calculator: to find C side in a right angle triangle)
#a = float(input("Side a: "))
#b = float(input("Side b: "))
#c = math.sqrt(pow(a, 2) + pow(b, 2))
#print(f"Side C is {c}")

#print("Website slicer!")
# Website1 = "http://google.com"
# Website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print(Website1[slice])
# print(Website2[slice])
# copy_list = Website1[:]
# print(copy_list)

#if statement = a block of code that will execute if its condition is true
#age = int(input("How old are you? "))
#if age == 100:
    #print("you are a century old")
#elif age >= 18:
    #Print("You are an adult")
#elif age < 0:
    #print("You havent been borned yet")
#else:
    #print("You are a child")

#calculator program
#operator == input("choose an operator (+ - * /): ")
#num1 = input("First numbers: ")
#num2 = input("Second numbers: ")
#if operator == "+":
 #   print(num1 + num2)
#if operator == "-":
 #   print(num1 - num2)
#if operator == "*":
 #   print(num1*num2)
#if operator == "/":
 #   print(num1/num2)
#else :
 #   print(f"{operator} isnt a valid operator")

#madlibs game
#noun = input("Choose a noun (female Person): ")
#Adjective = input("choose an adjective (description): ")
#verb = input("choose a verb (action with "ing"): ")
#print(f"I went home and saw {noun}")
#print(f"She was {verb} and laughing")
#print(f"I find it really {Adjective}")

#print("This is a weight conversion program.")
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or pounds? (K or L) ")
# if unit == "K":
#     weight = weight * 2.205
#     unit = "lbs"
# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs"
# else :
#     print(f"Your {unit} isnt valid.")
# print(f"Your weight is {round(weight, 1)} {unit}") 

#temperature conversion program
#for ° = Hold Alt, type 0176 on the numeric keypad, then release Alt.

# measurement = input("Choose a measurement (C for Celsius, F for Fahrenheit): ")

# if measurement == "C":
#     Celsius = float(input("Enter the value: "))
#     conversion = (Celsius * 9/5) + 32
#     print(f"{Celsius}°C is {conversion}°F")
# else :
#     Fahrenheit = float(input("Enter the value: "))
#     conversion = (Fahrenheit - 32) * 5/9
#     print(f"{Fahrenheit}°F is {conversion}°C")

#logical operators = execute the program if conditions are met
# or = either one of the conditions is true
# and = both conditions are true
# not = inverts the condition from true to false or vice versa

# temp = int(input("What is the temperature in Celsius? ")) 
# is_raining = input("Is it raining? (yes/no)")
# if is_raining == "yes":
#     is_raining = True
# else:
#     is_raining = False

# if temp > 35 or is_raining:
#     print("I can't go out")
# else:
#     print("I can go out")

# print("This a fight weigh in program")

# weight = float(input("Enter your weight (in kilograms): "))
# height = float(input("Enter your height (in centimeters): "))

# if weight <= 65 and height <= 170:
#     print("You are in the light weight category")
# elif weight <= 75 and height <= 175:
#     print("You are in the middle weight category")
# else:
#     print("You are in the heavy weight category")

# print("Give me your username.")
# print("must contain only letters, no numbers and spaces.")

# username = input("Enter your username: ")

# if not username.isalpha() :
#       print("You entered wrong! Only letters! and no spaces.")
# else :
#       print("You entered correctly!") 

# OR

# username = input("Enter your username:")

# if len(username) > 12 :      
#     print("Your username can't be more than 12 characters.")
# elif username.find(" ") != -1 :     # OR if not username.find(" ") == -1:
#     print("Your username can't contain spaces.")
# elif not username.isalpha() :
#     print("Your username can't contain numbers.")
# else :
#     print(f"Welcome, {username}!")

#compound interest calculator
# principle = 0 
# interest = 0
# time = 0

# while True :
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0 :
#         print("Principle can't be less or equal to zero.")
#     else :
#         break

# while True :
#     interest = float(input("Enter the interest rate amount: "))
#     if interest < 0 :
#         print("The interest rate can't be less or equal to zero.")
#     else :
#         break
    
# while True :
#     time = int(input("Enter the time in years: "))
#     if time < 0 :
#         print("Time can't be less or equal to zero.")
#     else :
#         break

# total = principle * pow((1 + interest/100), time)

# print(f"Your balance after {time} years is: ${total: .2f}")

# OR 
# answer = random.randint(0,101)
# print("Guess a random number from 1-100")

# counter = 0

# while True: 

#     counter += 1

#     guess = int(input("Enter your guess: "))
#     if guess == answer :
#         print(f"Your guess is correct. It took you {counter} tries.")
#         break
#     elif guess > answer : 
#         print("Too High")
#     else :
#         print("Too Low")

# Rock, Paper, Scissor game
# options = ("rock", "paper", "scissor")

# running = True

# while running:

#     player = None
#     computer = random.choice(options)

#     while player not in options: 
#         player = input("Choose (rock, paper, scissor): ").lower()

#     print(f"Computer chose {computer}.")
#     print(f"Player chose {player}.")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissor":
#         print("You Win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissor" and computer == "paper":
#         print("You win!")   
#     else:
#         print("You lose!")
#     if not input("Do you want to play again? (y/n): ").lower() == "y":
#         running = False
#         print("Thanks for playing!")
