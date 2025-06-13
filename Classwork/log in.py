attempts = 3
real_name = "admin"
real_pass = "pro69"

# while attempts != 0:
    
#     name = input("Enter your username: \n")
#     password = input("Enter your password: \n")

#     name = name.lower()
#     password = password.lower()

#     if name == real_name and password == real_pass:
#         print("Access authorized!")
#         break
    
#     else:
#         attempts -=1
#         print("Your username or password is incorrect.")
#         print(f"You have {attempts} left.")
#         continue

for attempts in range(3, 0, -1):
    name = input("Enter your username: \n")
    password = input("Enter the password: \n")

    name = name.lower()
    password = password.lower()

    if name == real_name and password == real_pass:
        print("Access authorized!")
        break

    else:
        print("Username or password is incorrect.")
        print(f"You have {attempts} attempts left.")
        continue
    


    