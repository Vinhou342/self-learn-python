print()
check = input("Enter your check for interest: \n")
month = input("Enter the amount of months: \n")

check = float(check)
month = int(month)

if check <= 500:
    interest = 0
elif check <= 1000:
    interest = 0.07
else :
    interest = 0.15

calculation = check * interest * month 
check += calculation

print(f"After the interest, your check after {month} months,")
print(f"your new check is {check:.2f}.")