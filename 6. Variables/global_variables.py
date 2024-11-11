"""Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside."""

# Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Create a variable inside a function, with the same name as the global variable


x = "awesome"

def myfunc2():
    x ="fantastic"
    print("Python is " + x)


myfunc2()

print("Python is "+ x)

"""The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword."""

def myfunc3():
    global x
    x = "fantastic"

myfunc3()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.

"""Example
To change the value of a global variable inside a function, refer to the variable by using the global keyword:"""

x = "awesome"
print(x)
def myfunc4():
    global x 
    x = "fantastic"

myfunc4()
print("Python is " + x)