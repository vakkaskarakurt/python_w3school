# Python Assignment Operators
# Operators used to assign values to variables

x = 5  # Initialize
print(f"Initial x: {x}\n")

# Basic Math Operators
x = 5   # Basic assignment 
print(f"x = 5: {x}")

x += 3  # Add (x = x + 3)
print(f"x += 3: {x}")

x -= 3  # Subtract
print(f"x -= 3: {x}") 

x *= 3  # Multiply
print(f"x *= 3: {x}")

x /= 3  # Divide 
print(f"x /= 3: {x}")

x %= 3  # Modulus (remainder)
print(f"x %= 3: {x}")

x //= 3 # Floor divide
print(f"x //= 3: {x}")

x **= 3 # Power
print(f"x **= 3: {x}\n")

# Bitwise Operators
x = int(x)  # Convert to integer

x &= 3  # AND
print(f"x &= 3: {x}")

x |= 3  # OR
print(f"x |= 3: {x}")

x ^= 3  # XOR
print(f"x ^= 3: {x}")

x >>= 3 # Right shift
print(f"x >>= 3: {x}")

x <<= 3 # Left shift
print(f"x <<= 3: {x}\n")

# Walrus Operator (Python 3.8+)
print(f"Walrus: (x := 3) -> {(x := 3)}")
print(f"Final x: {x}")