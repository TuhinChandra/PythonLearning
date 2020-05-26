print('Variables examples are here...')
x = 10
# Anything in python is an Object unlike other languages
print('x=', x, sep='')
print('type of x :', type(x))
print('id of x :', id(x))
y = 15
print('y=', y, sep='')
print('id of y :', id(y))

# Now see the id of y will change to id of x
y = 10
print('# Now see the id of y has changed to id of x')
print('y=', y, sep='')
print('id of y :', id(y))

# Objects are immutable in python
x = x + 1
print('# Objects are immutable in python thus it would change its id to new')
print('x=', x, sep='')
print('id of x :', id(x))
print('y=', y, sep='')
print('id of y :', id(y))

# Variables of any type can be changed to any other at any time
x = 3.5
print('# Variables of any type can be changed to any other at any time')
print('x=', x, sep='')
print('type of x :', type(x))
x = 'It\'s a String'
print('x=', x, sep='')
print('type of x :', type(x))
