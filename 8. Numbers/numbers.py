"""Python Numbers
There are three numeric types in Python:

int
float
complex"""

# Variables of numberic types are created when you assign a value to them:

x = 1 # int
y = 2.8 # float
z = 1j # complex

# To verify the type of any object in Python, use the type() function:

print(type(x))
print(type(y))
print(type(z))

"""Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited 
length."""

# Integers:

x = 1
y = 32532532532535325
z = -321541254

print(type(x))
print(type(y))
print(type(z))

"""Float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals."""

# Floats
x = 1.10
y =1.0
z =-44.22

print(type(x))
print(type(y))
print(type(z))

"""Float can also be scientific numbers with an "e" to indicate the power of 10. """

# Floats:

x = 35e3
y = 12E4
z = -55.6e100

print(type(x))
print(type(y))
print(type(z))

"""Complex
Complex numbers are written with a "j" as the imaginary part:"""

x = 3+5j
y =5j
z =-5j

print(type(x))
print(type(y))
print(type(z))


"""Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:"""

x = 1 # int 
y = 2.8 # float
z = 1j # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# conver from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""You cannot convert complex numbers into another number type."""


"""Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:"""

import random

print(random.randrange(1,10))
