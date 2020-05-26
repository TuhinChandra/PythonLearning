print('break keyword examples are here...')
str1 = input('Enter a string :')
for i in str1:
    if i == ' ':
        print()
        print('encountered whitespace, breaking the loop')
        break
    print(i, end=' |')
print('for loop execution completed')
