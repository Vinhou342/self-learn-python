
#indexing = accessing a single element from a sequence using [] (indexing operator)
#          [start:stop:step]

security_number = "1234 5678 9012 3456"

first_quarter = security_number[0:4]
second_quarter = security_number[5:9]
third_quarter = security_number[10:14]
fourth_quarter = security_number[15:]

print(first_quarter)
print(second_quarter)
print(third_quarter)
print(fourth_quarter)

last_digits = security_number[-4:] 
# even though negative index starts from the last, it still execute from left to right

print(f"Your security number is XXXX-XXXX-XXXX-{last_digits}")