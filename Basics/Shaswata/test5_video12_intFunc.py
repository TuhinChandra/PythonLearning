print('int function examples are here...')
x = '1100'
print("x =", x)
print("type of x :", type(x))

# int string -> int
print('int string -> int')
y = int(x)  # default base is 10
print("y =", y)
print("type of y :", type(y))

# binary string -> int
print('binary string -> int')
z = int(x, 2)
print("z =", z)

# ValueError: invalid literal for int() with base 2: '1234'
x = '12347'
print("x =", x)
# y = int(x, 2)

# Oct string -> int
print('Oct string -> int')
y = int(x, 8)
print("y =", y)

# Hex string -> int
print('Hex string -> int')
x = '1a'
print("x =", x)
y = int(x, 16)
print("y =", y)

