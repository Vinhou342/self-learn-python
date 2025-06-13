#List comprehension     = A concise way to create list in python
#                         Compact and easier to read than traditional loops
#                         [Expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
    
# print(doubles)

# We can shorten the codes like these:

# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# squares = [y * y for y in range(1, 11)]
# print(squares)

# fruits = ["kiwi", "peach", "dragonfruit", "durian"]
# fruits = [fruit.capitalize() for fruit in fruits]

# print(fruits)

# numbers = [1, -4, 7, 9, -12]

# positive_nums = [num for num in numbers if num > 0]
# even_nums = [num for num in numbers if num % 2 == 0]

# print(positive_nums)
# print(even_nums)

grades = [69, 53, 75, 88, 92]

passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
