print('Assignment operator examples are here...')
# always right hand values are assigned to left hand operators
x = 10  # L value <- R value
print('x =', x)

# assignments are done in order of left hand side
x, y, z = 10, 15, 20
print('x =', x, 'y =', y, 'z =', z)

# assignment operator is right associative
x = y = z = 25
print('x =', x, 'y =', y, 'z =', z)

print('# assignment operator like +=, -=, *=, /= works similar like other programming languages')
