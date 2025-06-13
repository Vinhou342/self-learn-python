print("This is a BMI calculator!")

name = input("What is your name: \n")

age = input("How old are you? \n")

weight = input("Enter your weight (in kilos): \n")
weight = float(weight)

height = input("Enter your height (in meters) \n")
height = float(height)

calculation = weight / (height ** 2)

print(f"Hello {name}! Age {age} years old.")
print(f"Your BMI calculation is {calculation}")

