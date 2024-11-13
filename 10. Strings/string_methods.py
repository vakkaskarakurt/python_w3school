# 1. capitalize()
text = "hello world"
print(text.capitalize())  # "Hello world"

# 2. casefold()
text = "HELLO"
print(text.casefold())  # "hello"

# 3. center()
text = "Python"
print(text.center(10, "*"))  # "**Python**"

# 4. count()
text = "hello hello"
print(text.count("hello"))  # 2

# 5. encode()
text = "hello"
print(text.encode())  # b'hello' (in UTF-8)

# 6. endswith()
text = "filename.txt"
print(text.endswith(".txt"))  # True

# 7. expandtabs()
text = "Hello\tworld"
print(text.expandtabs(8))  # "Hello   world"

# 8. find()
text = "find the needle"
print(text.find("needle"))  # 9

# 9. format()
text = "My name is {name} and I am {age} years old."
print(text.format(name="Alice", age=25))  # "My name is Alice and I am 25 years old."

# 10. format_map()
info = {"name": "Alice", "age": 25}
print("My name is {name} and I am {age} years old.".format_map(info))

# 11. index()
text = "locate the needle"
print(text.index("needle"))  # 10

# 12. isalnum()
text = "Python3"
print(text.isalnum())  # True

# 13. isalpha()
text = "Python"
print(text.isalpha())  # True

# 14. isascii()
text = "Hello!"
print(text.isascii())  # True

# 15. isdecimal()
text = "12345"
print(text.isdecimal())  # True

# 16. isdigit()
text = "12345"
print(text.isdigit())  # True

# 17. isidentifier()
text = "variable_name"
print(text.isidentifier())  # True

# 18. islower()
text = "hello"
print(text.islower())  # True

# 19. isnumeric()
text = "12345"
print(text.isnumeric())  # True

# 20. isprintable()
text = "Hello\nWorld"
print(text.isprintable())  # False (because of newline)

# 21. isspace()
text = "   "
print(text.isspace())  # True

# 22. istitle()
text = "This Is A Title"
print(text.istitle())  # True

# 23. isupper()
text = "HELLO"
print(text.isupper())  # True

# 24. join()
words = ["hello", "world"]
print(" ".join(words))  # "hello world"

# 25. ljust()
text = "left"
print(text.ljust(10, "-"))  # "left------"

# 26. lower()
text = "HELLO"
print(text.lower())  # "hello"

# 27. lstrip()
text = "    hello"
print(text.lstrip())  # "hello"

# 28. maketrans()
intab = "abc"
outtab = "123"
trantab = str.maketrans(intab, outtab)
text = "abcde"
print(text.translate(trantab))  # "123de"

# 29. partition()
text = "apple and orange"
print(text.partition("and"))  # ('apple ', 'and', ' orange')

# 30. replace()
text = "hello world"
print(text.replace("world", "Python"))  # "hello Python"

# 31. rfind()
text = "find the last 'the'"
print(text.rfind("the"))  # 14

# 32. rindex()
text = "locate the last 'needle'"
print(text.rindex("needle"))  # 18

# 33. rjust()
text = "right"
print(text.rjust(10, "-"))  # "-----right"

# 34. rpartition()
text = "apple and orange"
print(text.rpartition("and"))  # ('apple ', 'and', ' orange')

# 35. rsplit()
text = "apple,orange,banana"
print(text.rsplit(",", 1))  # ['apple,orange', 'banana']

# 36. rstrip()
text = "hello     "
print(text.rstrip())  # "hello"

# 37. split()
text = "apple orange banana"
print(text.split())  # ['apple', 'orange', 'banana']

# 38. splitlines()
text = "line1\nline2\nline3"
print(text.splitlines())  # ['line1', 'line2', 'line3']

# 39. startswith()
text = "hello world"
print(text.startswith("hello"))  # True

# 40. strip()
text = "   hello   "
print(text.strip())  # "hello"

# 41. swapcase()
text = "Hello World"
print(text.swapcase())  # "hELLO wORLD"

# 42. title()
text = "this is a title"
print(text.title())  # "This Is A Title"

# 43. translate()
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
text = "hello"
print(text.translate(trantab))  # "h2ll4"

# 44. upper()
text = "hello"
print(text.upper())  # "HELLO"

# 45. zfill()
text = "42"
print(text.zfill(5))  # "00042"
