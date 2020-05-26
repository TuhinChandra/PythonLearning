print('if else examples is here...')
# if-else blocks are used to compare between two values
x = int(input('Enter 1st number : '))
y = int(input('Enter 2nd number : '))
if x > y:
    print('Executing inside if block...')
    print('maximum value is x :', x)
elif x == y:
    print('Executing inside elif block...')
    print('both values are equal', x)
else:
    print('Executing inside else block...')
    print('maximum value is y :', y)
print('Execution of compound if-else block is done...')
