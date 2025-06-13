#Dictionaries = a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA":"Washinton D,C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# if capitals.get("Japan"):
#     print("That capital is in the library.")
# else :
#     print("That capital isn't in the library.")

# capitals.update({"Germany":"Berlin"})               #insert a new item in the library
# capitals.update({"USA":"Detroit"})                    #change a value of a key
# capitals.pop("China")                               #remove the whole item from library
# capitals.popitem()                                  #remove the latest item in library
# capitals.clear()                                    #clear the whole dictionary
# keys = capitals.keys()                              #return only the keys of the items
# values = capitals.values()                          #return only the values of the items
# items = capitals.items()                            #reurn the whole item in the library
for key, value in capitals.items():
    print(f"{key}: {value}")

#concession stand program

menu = {"Pretzel": 3.00,
        "Nachos": 3.00,
        "Lemonade": 1.00,
        "Popcorn": 2.00}

cart = []
total = 0

# print("---------MENU---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:2f}")
# print("----------------------")

# while True:
#     food = input("Choose a food (q to quit): ").capitalize()
#     if food == "Q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#     print()

# print("---------YOUR PURCHASE---------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
# print()

# print(f"Your total is ${total:.2f}")