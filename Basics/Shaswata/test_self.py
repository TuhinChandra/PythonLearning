# # #
# # # from __future__ import print_function
# # #
# # # import sys
# # # from time import sleep
# # #
# # # fp = sys.stdout
# # # print('Do you want to continue (Y/n): ', end='')
# # # fp.flush()
# # # sleep(50)
# #
# #
# # # from abc import ABC, abstractmethod
# # #
# # #
# # # class A(ABC):
# # #
# # #     def __init__(self, x):
# # #         print('Inside __init__ method of class A.')
# # #         self.x = x
# # #         print('value of x :', x)
# # #
# # #     @abstractmethod
# # #     def abs_func(self):
# # #         pass
# # #
# # #
# # # class B(A):
# # #
# # #     def __init__(self, x):
# # #         print('Inside __init__ method of class B.')
# # #         super().__init__(x)
# # #         self.abs_func()
# # #         print('value of x :', self.x)
# # #
# # #     def abs_func(self):
# # #         print('abs_func is called.')
# # #         self.x = self.x * 10
# # #
# # #
# # # a = B(5)
# # # print(a.x)
# # #
# # # print(type(None))
# # # print(id(None))
# # import sys
# #
# #
# # # x = "le halua..."
# # # print(sys.getrefcount(x))
# # #
# # # x = 10
# # # print(x)
# # # print(type(x))
# # # x = 'hei'
# # # print(x)
# # # print(type(x))
# #
# # # print(R'wow, \n is not working...!!!', flush=True)
# # # print('Hei there...')
# # #
# # # def formatted_func(func):
# # #     print('Inside formatted_func.')
# # #
# # #     def print_func(*args, **kwargs):
# # #         print('-' * 30)
# # #         func(*args, **kwargs)
# # #         print('-' * 30)
# # #
# # #     print('exiting formatted func.')
# # #     return print_func
# # #
# # #
# # # @formatted_func
# # # def say_welcome(name):
# # #     print('Welcome!', name)
# # #
# # #
# # # @formatted_func
# # # def say_hello(name, msg):
# # #     print('Hello, ', name, '\n', msg, sep='')
# # #
# # #
# # # say_hello('Shaswata', 'Hope you are doing good.')
# #
# # x = '12'
# # print(x)
# # print(type(x))
# # print(id(x))
# # # x = x + 1             impossible
# # y = int(x)
# # print(y)
# # print(type(y))
# # print(id(y))
# # print(y)
# # y = str(y)
# # print(y)
# # print(type(y))
# # print(id(y))
# x = int(input("Enter something:"))
# print(x)
# print(type(x))
# lst = list()
# lst.append(10)
# lst.append("str")
# print(lst)
# print(id(lst))
# lst.append(3.5)
# print(lst)
# print(id(lst))
# x = 10
# print(x)
# print(id(x))
# print(id(10))
# print(id(9999999999))

lst = list()
lst.append(10)
lst.append("string")
lst.extend("shaswata")
print(lst)
str1 = "shaswata"



