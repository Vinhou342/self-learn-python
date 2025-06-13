num1 = input("Enter your first number: \n")
num2 = input("Enter your second number; \n")

num1 = int(num1)
num2 = int(num2)

if num1 > num2:
    print(f"The number {num1} is greater than {num2}.")
elif num1 < num2:
    print(f"The number {num1} is less than {num2}.")
else:
    print(f"Both numbers are equal")