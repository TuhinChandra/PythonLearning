print('for and range examples are here...')
print('# range itself is a class')
print('what range(5) returns :', range(5))
print('type of range(5) :', type(range(5)))
print()
# for examples are following
print('# range function with one parameter')
for i in range(5):
    print('i=', i, sep='', end=' ')
print()
print('# range function  with two parameters')
for i in range(5, 10):
    print('i=', i, sep='', end=' ')
print()
print('# range function  with three parameters')
for i in range(25, 5, -5):
    print('i=', i, sep='', end=' ')
print()
print('# for loop as a string iterator')
for i in 'Hei, there...':
    print(i, end='|')
