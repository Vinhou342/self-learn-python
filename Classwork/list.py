# nums = [2, 3, 4, 8, 9]

# for index, val in enumerate(nums): # can also access its index
#     print(f"index {index}:{val}") 

# Slice odd and even list
# numbers = [34, 21, 56, 78, 9, 42, 17, 65, 29, 83]

# # # Using filter
# even_index_items = list(filter(lambda x: x[1] % 2 == 0, enumerate(numbers)))
# odd_index_items = list(filter(lambda x: x[1] % 2 != 0, enumerate(numbers)))

# even_values = [x[1] for x in even_index_items]
# odd_values = [x[1] for x in odd_index_items]

# print("Original List:", numbers)
# print("Even Items:", even_values)
# print("Odd Items:", odd_values) 

#Even Items: [(0, 34), (2, 56), (3, 78), (5, 42)]
#Odd Items: [(1, 21), (4, 9), (6, 17), (7, 65), (8, 29), (9, 83)]

# the x[1] refers to the value
# the x[0] refers to the index (of the original list)


# OR
# odd = []
# even = []

# for i in numbers:
#   if i % 2 == 0:
#     even.append(i)

#   elif i % 2 == 1:
#     odd.append(i)

# print(f"Odd: {odd}")
# print(f"Even: {even}")


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# temps_k = [310, 295, 300, 285, 290, 280, 278]

# weekday_k = temps_k[0:5]

# weekday_c = [k - 273.15 for k in temps_k]

# # OR
# # weekday_c = []
# #for i in weekday_k:
# #    cel = i - 273.15
# #    weekday_c.append[cel]

# print(f"Weekday in celcius: {weekday_c}")
# print(f"Total celcius in weekday: {sum(weekday_c)}")
# print(f"Average celcius during weekday: {sum(weekday_c)//len(weekday_c)}")

# list = ["Friday", "Monday", "Sunday", "tuesday"]

# print(min(list))

# Friday is the output because F has the minimum decimal among the ASCII table
# uppercase letters come first before lowercase 
# we only consider the first letter 

# numbers should come before uppercase but it doesn't work

# # Example 1
# nums = [1, 2, 3, 4]
# squares = [x**2 for x in nums]
# print(squares) # Output: [1, 4, 9, 16]
# # Example 2
# numbers = [1, 5, 2, 8, 3, 7, 10, 6, 4, 9]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers) # Output: [2, 8, 10, 6, 4]


nums = [1, 2, 3, 4]
squares = [x**2 for x in nums]
print(squares) # Output: [1, 4, 9, 16]
# Example 1 using traditional loops
nums = [1, 2, 3, 4]
squares = [] # Initialize an empty list to store the squares
for x in nums:
    squares.append(x**2) # Append the square of each number to the list
print(squares) # Output: [1, 4, 9, 16]




