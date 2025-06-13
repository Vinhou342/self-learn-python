# shopping cart program

foods = []
prices = []
total = 0 

while True :
    food = input("Enter a food you would like to purchase: (q to quit) ")
    if food.lower() == "q":
        break
    else :
        price = float(input("Enter the price for that item: $ "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods :
    print(food, end= " ")
print()

for price in prices :
    total += price

print(f"Your total is ${total} ")