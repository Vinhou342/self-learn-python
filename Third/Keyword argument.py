# Keyword argument = an argument preceded by an identifier
#                    helps with readability
#                    order of arguments don't matter
#                    1. positional , 2. default , 3. KEYWORD , 4. arbitrary 

# def hello(greetings, title, first, last):
#     print(f"{greetings} {title}{first} {last}!")

# hello(title = "Dr. ", last = "Dover", first = "Ben", greetings = "Fuck you,")

# for x in range(1, 10):
#     print(x, end = " ")

# print("1", "2", "3", "4", "5", sep = "-")


#generate a phone number

def get_num(country, area, first, last):
    return f"+{country}-{area}-{first:03}-{last}"

phone_num = get_num(country = 855, area = 1201, first = 69, last = 333)

print(phone_num)