print('list examples are here...')
# lst = list() or lst = [] can be used to generate empty list
print('list in python is a mutable object...')
lst = [10, 'abc', 20, "def", 30, 40, 50, 60]  # lists are heterogeneous, means can have various diff data types
print(lst)
print('Values in the list are :', end=' ')
for i in lst:
    print(i, end=' ')
print()
slicedLst = lst[1: 5]
print(slicedLst)
print('id of lst :', id(lst))
print('id of slicedLst :', id(slicedLst))
lst[0] = 'xyz'
print(lst)
print('id of lst :', id(lst))
