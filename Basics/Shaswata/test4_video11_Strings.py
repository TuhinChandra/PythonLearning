print('String examples are here...')
str1 = '1st sample string...'
str2 = "2nd sample string..."
print(str1, str2, sep="\n")

# length of a string
str3 = 'sample string...'
lenStr3 = len(str3)
print("length of str3 :", lenStr3)
# Conversion string to int, float classes...

# string -> int
x = '100'
print("x =", x)
print("type of x :", type(x))
print('Converting string x to int y...')
y = int(x)  # string -> int
print("y =", y)
print("type of y :", type(y))

# string -> float
x = '150.56'
print("x =", x)
print("type of x :", type(x))
print('Converting string x to float y...')
y = float(x)  # string -> float
print("y =", y)
print("type of y :", type(y))

print('Cannot convert float string x to int z...')
# z = int(x)                            ValueError: invalid literal for int() with base 10: '150.56'
# print("z =", z)
# print("type of z :", type(z))

# String concatenation...
print('String concatenation...')
str1 = "Hello,"
str2 = "How are you ?"
str3 = str1 + ' ' + str2
print(f"str3:{str3}")
print(f"length of str3: {len(str3)}")

# Strip string...
print('Strip string...')
str4 = '   apple  '
print(f"str4(--- are to show white spaces only, not a part of str4):---{str4}---")
print('lstrip str4 :', str4.lstrip(), '**', sep='')
print('rstrip str4 :', str4.rstrip(), '**', sep='')
print('strip str4 :', str4.strip(), '**', sep='')

