"""Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:"""

# # You will get an error if you use double quotes inside a string that is surrounded by double quotes:
# txt = "We are the so-called  "Vikings" from the north.

"""To fix this problem, use the escape character \":"""
# The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."
print(txt)



#### Other escape characters used in Python:

txt = 'It\'s alright.' # Single Quote
print(txt)

txt = "This will insert one \\ (backslash)." #Backslash
print(txt)

txt = "Hello\nWorld!" #New Line
print(txt)

txt = "Hellooo Vakkas\rWorld!" #Carriage Return
print(txt)

txt = "Hello\tWorld!" #Tab
print(txt)

#This example erases one character (backspace):
txt = "Hello \bWorld!" #Backspace
print(txt)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157" #Octal value
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f" # Hex value
print(txt) 



