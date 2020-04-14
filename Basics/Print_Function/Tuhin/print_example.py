#WAP to print multiple strings, an int and a float value using a single print statement in python.
#exampleOutput: Hello Second String int value: 10 float value: 55.15
firstString="First String"
secondString="Second String"
integerValue=10
floatvalue=55.55
print(firstString,secondString,integerValue,floatvalue,sep='')
#To remove the newline character from a string in Python, use its .rstrip() method, like this:
print('A line of text.\n')
print('*'*20)
print('A line of text.\n'.rstrip())
print('*'*20)
print('Please wait while the program is loading')

#you can’t use double quotes for the literal and also include double quotes inside of it,
# because that’s ambiguous for the Python interpreter
#"My favorite book is "Python Tricks""  # Wrong!
print('My favorite book is "Python Tricks"')
print("My favorite book is 'Python Tricks'")
#Alternatively, you could use escape character sequences mentioned earlier,
# to make Python treat those internal double quotes literally as part of the string literal:
print("My favorite book is \"Python Tricks\"")
#This goes wrong for file path in windows
#print('C:\Users\jdoe')
#Fortunately, you can turn off character escaping entirely with the help of raw-string literals.
#Simply prepend an r or R before the opening quote, and now you end up with this:
print(r'C:\Users\jdoe')

paragraph = '''
     This is an example
     of a multi-line string
     in Python.
     '''

print(paragraph)

#To remove indentation from a multi-line string,
# you might take advantage of the built-in textwrap module:
import textwrap
print(textwrap.dedent(paragraph).strip())
import os
#Concat String
print('Hello, ' + os.getlogin() + '! How are you?')

#In fact, there are a dozen ways to format messages in Python. I highly encourage you to take a look at f-strings, introduced in Python 3.6, because they offer the most concise syntax of them all:
print(f'Hello, {os.getlogin()}! How are you?')
