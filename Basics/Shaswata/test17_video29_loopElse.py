import math
print('loop else examples are here...')
n = int(input('Enter a number: '))
i = 2
while i <= math.sqrt(n):
    if n % i == 0:
        print('The number: ', n, 'is not a prime number')
        break
    i += 1
else:
    print(n, 'is Prime Number')
print('Thank you!!!')
