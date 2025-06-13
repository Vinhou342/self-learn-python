#slicing = create a substring by extracting elements from another string index[], slicing(), [start:stop:step]
name = "Bro_Hou"
First_Name = name[:3]
Last_Name = name[4:]
#[start: stop: step]
# start = the index where the slicing will start​​ (default is 0)
# stop = the index where the slicing will stop (default is the end of the string)
# step = the number of characters to move forward (default is 1)
Funky_Name = name[::3] #skip every second and third character
Funky_Name2 = name[::2] #skip every second character
Reversed_Name = name[::-1]
print(Funky_Name)
print(Funky_Name2)