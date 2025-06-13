#default arguments = a default value for certain parameters
#                    default is used when that argument is omitted
#                    makes your arguments more flexible, reduces # of arguments
#                    1. positional , 2. default , 3. keyword , 4. arbitrary 

# def net_price(price, discount = 0.1 , tax = 0.05):
#     return price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.2))
# print(net_price(500, 0.2, 0))


#times up program

import time

def count(end, start = 0):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")
count(10)