#iterables      = an object/argument that return its element one at a time, 
#                 allowing it to be iterated in a loop.

numbers = [1, 2, 3, 4, 5]                                   #list
numbers2 = (1, 2, 3, 4, 5)                                  #tuples
fruits = {"apples", "kiwi", "orange", "watermelon"}         #sets cant be reversed

# for number in reversed(numbers):
#     print(number)

username = "Astolfo femboy"

# for name in username:
#     print(name, end = " ")

kink_type = {"Vinhou": "Mommy", 
             "Sunheng": "Thighs",
             "Thean": "Tomboy"}

for key, value in kink_type.items():
    print(key, value)



