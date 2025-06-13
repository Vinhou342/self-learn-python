#collections = single "variable" used to store multiple values
#   list    = [] ordered and changeable. Duplicates OK. 
#   set     = {} unordered and immutable. but add/remove OK. No duplicates.
#   tuple   = () ordered and changeable. Duplicates OK. Faster

fruits = ["apples", "bananas", "oranges", "pineapples"]
print(fruits[::2])              #skip every second element
print(dir(fruits))              #shows all the extended functions
print(help(fruits))             #shows all the extended functions and elaborate them
print(len(fruits))
print("pineapples" in fruits)

fruits[0] = "Kiwi"               #change element"
fruits.append("Kiwi")
fruits.remove("apples")
fruits.insert(0, "jackfruit")
fruits.sort()                   #sort alphabetically
fruits.reverse()  
fruits.clear()
print(fruits.index("bananas"))          #prints the order number of that element
print(fruits.count("bananas"))          #count the modes of that element

for fruit in fruits:
    print(fruit)

cats = {"orange", "brittish", "sphinx", "tuxedo"}
print(dir(cats))              #shows all the extended functions
print(help(cats))             #shows all the extended functions and elaborate them
print(len(cats))
print("orange" in cats)

cats.add("Calico")
cats.remove("birttish")
cats.pop()                     #remove the first element but it will be randomized
cats.clear()                   #clear the set

print(cats)

meat = ("fish", "pork", "beef", "sausage")
print(dir(meat))              #shows all the extended functions
print(help(meat))             #shows all the extended functions and elaborate them
print(len(meat))
print("orange" in meat)
print(meat.index("pork"))
print(meat.count("beef"))