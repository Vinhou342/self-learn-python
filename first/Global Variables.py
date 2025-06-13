x = "Python"

def myfunc():
    x = "Java" 
    print("I love learning " + x)
myfunc()

print("I love learning " + x + " too.")

# OR

def myfunc():
    global x
    x = "C++"
    print("I mustn't forget " + x)
myfunc()