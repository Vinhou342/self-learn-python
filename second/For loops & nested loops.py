# For loops = execute a block of code a fixed number of times 
#             You can iterate over a range, string, sequence, etc. 

import time

# for counter in range(1,5):
#     print(counter)
# for x in reversed(range(1,5)):
#     print(x)
# for y in range(1, 6, 2): 
#     print(y)

# credit_card = "1234-5678-9012-3456"
# for z in credit_card:
#     print(z)

# for x in range(1, 21):
#     if x == 13 :
#         continue                #"continue" = to skip that one exact element 
#     else :
#         print(x)

# Nested Loop = a loop within another loop (outer, inner)
#               outer loop
#                  inner loop

for x in range(3):
    for y in range(1,10):
        print(y, end = " ")     #can use "\n" or ""
    print()                     #this "print()" here ends one repeatition with a new line

# rows = int(input("Enter the number of rows: "))

# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol you wanna use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end = " ")     #can use "\n" or ""
#     print() 


# countdown timer program

# my_time = int(input("Enter the time in seconds: " + "\n"))

# for x in range(my_time, 0, -1):
#     seconds = x % 60                        # "%" finds the remainder
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600) 
    
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")
