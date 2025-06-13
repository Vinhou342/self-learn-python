#2d collections

fruits =        ["apple", "Kiwi", "watermelon", "mango"]
meat =          ["chicken", "fish", "beef", "pork"]
vegetables =    ["celery", "cabbages", "bok choy"]

groceries = [fruits, meat, vegetables]
# OR you can write like this (not nice)

#groceries = [["apple", "Kiwi", "watermelon", "mango"], ["chicken", "fish", "beef", "pork"], ["celery", "cabbages", "bok choy"]]

# print(groceries)
# print(groceries[0])                         #this sets the fuits "list" as the "element" instead
# print(groceries[1])                         #this sets the meat "list" as the "element" instead
# print(groceries[1][1])                         #this chooses an exact element from one list
# print(groceries[2][2])                         #this chooses an exact element from one list

for collection in groceries :           #remove one list("[]")
    for food in collection :            #remove another set of list ("[]")
        print(food, end=" ")
    print()

