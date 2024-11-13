"""Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are
actually the same object, with the same memory location:"""

"""IS"""
#Returns True if both variables are the same object

x =["apple","banana"]
y =["apple","banana"]
z=x

print(x is z)

# returns True because z is the same object as x

print(x is y)

#returns False because x is not the same object as y, even if they have the same content

print(x ==y)
#to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y


"""IS NOT"""
#Returns True if both variables are not the same

x =["apple","banana"]
y =["apple","banana"]
z=x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x!=y)
#to demonstrate the difference between "is not" and "!=": this comparison returns False because x is equal to y