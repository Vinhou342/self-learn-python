menu = {"Pretzel": 3.00,
        "Nachos": 3.00,
        "Lemonade": 1.00,
        "Popcorn": 2.00}

cart = []
total = 0
is_running = True

print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------")

while is_running:
    food = input("Choose a food (q to quit): ").capitalize()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    print()

print("---------YOUR PURCHASE---------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")
print()

print(f"Your total is ${total:.2f}")





