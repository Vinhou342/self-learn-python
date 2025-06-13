# while loops = execute some code while some conditions remain true

name = input("GIVE ME YOUR NAME: ")

while name == "":
    print("YOU DIDN'T GIVE ME YOUR NAME!")
    name = input("GIVE ME YOUR NAME: ")
print(f"THANK YOU {name}!") 

# another example, with break statement

food = input("WHAT IS YOUR FAVORITE FOOD? (q to quit) ")

while not food == "q":
    print(f"YOU LOVE {food}!")
    food = input("WHAT IS YOUR OTHER FAVORITE FOOD? (q to quit)")

print("BYE MONKEY!")

# Another example

number = int(input("GIVE ME A RANDOM NUMBER BETWEEN 1 TO 10! "))

while number < 1 or number > 10 :
    print("MONKEY, 1 TO 10!")
    number = int(input("GIVE ME A RANDOM NUMBER BETWEEN 1 TO 10! "))

print(f"Your number is {number}.")