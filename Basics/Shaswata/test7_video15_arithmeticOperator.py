print('Arithmetic operator examples are here...')
print('# exponent operator is right associative: [ 2**3**2 = (2 ** (3 ** 2)) = 2 ** 9 = 512 ]')
print('2 ** 3 :', 2 ** 3)
# exponent operator is right associative: [2**3**2 = (2**(3**2)) = 2**9 = 512]
print('2 ** 3 ** 4 :', 2 ** 3 ** 2)

print('# multiplication operator is left associative')
print('2 * 3 :', 2 * 3)
# multiplication operator is left associative: [2*3*5 = ((2*3)*5) = 6*5 = 30]
print('2 * 3 * 5 :', 2 * 3 * 5)

print('# Division operator is left associative: [12/6/2 = ((12/6)/2) = (2/2) = 1.0]')
print('6 / 2 :', 6 / 2)
# Division operator is left associative: [12/6/2 = ((12/6)/2) = (2/2) = 1.0]
print('12 / 6 / 2 :', 12 / 6 / 2)

print('# floor division results largest value less than the quotient')
print('10 // 3 :', 10 / 3)
# floor division results largest value less than the quotient
print('10 // -3 :', 10 // -3)

print('# modulo operator returns the remainder after division')
print('10 % 3 :', 10 % 3)
print('10 % 5 :', 10 % 5)

print('# addition and subtraction')
print('10 + 13 :', 10 + 13)
print('10 - 18 :', 10 - 18)

print('# () has highest precedence level...')
print('# ** has second highest precedence level with a right associativity...')
print('# *, /, //, % has third highest precedence level with a left associativity...')
print('# +, - has the lowest precedence level with a left associativity...')
# Due to precedence: [3 * 6 + 7 - 2 / 4 = (3*6)+7-(2/4) = 18+7-0.5 = 24.5]
print('3 * 6 + 7 - 2 / 4 :', 3 * 6 + 7 - 2 / 4)
