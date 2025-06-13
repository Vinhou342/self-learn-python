animals = ("Leopard", "Lion", "turtle", "rodent", "shark")
biomes = ("tundra", "rainforests", "sovanna", "dessert")
mixed = ("Jane", None, False, 3.14)

concat = animals + biomes + mixed

# print(concat)

replicate = ("X", "Y") * 3
# print(replicate)


def arithmetic(x, y):
    arith = (x+y, x-y, x*y, x/y)
    return arith
    
# print(arithmetic(2, 3))     # for value tuple
# print()

sum, sub, pro, div = arithmetic(2, 3)

print(pro)




