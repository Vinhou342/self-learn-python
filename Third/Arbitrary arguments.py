# *args         = allows you to pass multiple non-key arguments     (tuple)
# **kwargs      = allows you to pass multiple keyword arguments     (dictionaries)
#                * unpacking operator
#                1. positional , 2. default , 3. Keyword , 4. ARBITRARY

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3))

# OR

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1, 2, 3))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# def get_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# get_address(street = " 123 Fake St.",
#             Apt = "101",
#             City = "Detroit", 
#             State = "MI", 
#             Zip = "54321")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('City')} {kwargs.get('State')} {kwargs.get('Zip')}")

shipping_label("Dr.", "Spongebob", "Harold", "Squarepants", "III",
               street = "123 Fake St.",
               Apt = "101",
               City = "Detroit", 
               State = "MI", 
               Zip = "54321")

