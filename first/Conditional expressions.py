user_role = "admin" 

print ("full access" if user_role == "admin" else "restricted access")

temp = input("Enter the temperature: ")

print("It's hot." if int(temp) >=30 else "It's cold.")