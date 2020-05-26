print('continue keyword examples are here...')
str1 = input('Enter a string :')
for i in str1:
    if i == ' ':
        continue
    print(i, end=' |')
print()
print('for loop execution completed')
# another example taken from Shibaji paul video
n = int(input('Enter a number: '))
i = 1
while i <= n:
    if i % 2 == 0:
        i = i + 1
        continue

    print(i, end=' ')
    i = i + 1
print()
print('At the end of while')
