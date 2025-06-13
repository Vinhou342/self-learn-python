#format specifier = {value:format} format a value based on what flags are inserted

price1 = 3.14159
price2 = -41.932
price3 = 6900.691

print(f"price 1 is: ${price1:.2f}")
print(f"price 2 is: ${price2:.2f}") 
print(f"price 1 is: ${price1:10.2f}")   #10 is the width of the field and .2f is the number of decimal places
print(f"price 2 is: ${price2:010.2f}")  #0 is the fill character 
print(f"price 1 is: ${price1:<010}")     #< is the right alignment specifier of field 
print(f"price 2 is: ${price2:>010}")     #> is the left alignment specifier of field
print(f"price 1 is: ${price1:^010}")     #^ is the center alignment specifier of field
print(f"price 1 is: ${price1:+}") #+ is the sign specifier for positive numbers and negative remained constant
print(f"price 2 is: ${price2: }") #space is the sign specifier for positive numbers and negative remained constant
print(f"price 1 is: ${price1:,}") #, is the thousandth digit separator 
print(f"price 3 is: ${price3: ,.2f}")
