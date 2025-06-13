name = "Bro_Hou"

print(len(name))
print(name.find("o"))       
print(name.rfind("o")) #finds the last occurrence of the character
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit()) #checks if the string is a number
print(name.isalpha()) #false because there is an underscore "_"
print(name.isalnum()) #checks if the string is a number or letter

phone_number = input("Enter your phone number: ")

count_dash = phone_number.count("-") 
print(count_dash)

phone_number = phone_number.replace("-", " ")
print(phone_number)
