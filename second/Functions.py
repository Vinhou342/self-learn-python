#functions = a block of code that can run multiple times

# def fav_food():
#     food = input("What is your favorite food? ")
#     print(f"Your favorite food is {food}")

# fav_food()
# fav_food()
# fav_food() #you recall three times = three repetitions
  
#OR

# def fav_person(name, relationship):
#     print(f"Your favorite person is {name} <3")
#     print(f"She is your {relationship}.")
    
# fav_person("Nika", "Kitty #1")
# fav_person("Mika", "Kitty #2")
# fav_person("Tika", "Kitty #3")

# def display_invoice(name, amount, due_date):
#     print(f"Hello {name}!")
#     print(f"Your bill of ${amount:2f} is due on {due_date}!")

# display_invoice("Nhou", 99.99, "1st February")


#return = statement used to end a function and send a result back to the caller

def date_of_birth(day, month):
    day = (f"{day:02}")
    month = month.capitalize()
    return day + " " + month

birthday = date_of_birth(9, "May") 

print(birthday)