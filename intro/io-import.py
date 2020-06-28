## --------------- I/O & Modules ---------------


# Imports
# When our program grows bigger, it is a good idea to break it into different modules.
# A module is a file containing Python definitions and statements. Python modules have a filename and end with the extension .py.

# import math
# print(pi);

from math import pi
print(pi);




# Output
 
a = 'Hello';
print('This sentence is output to the screen', a);

# Syntax for print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# objects = value(s) to be printed
# sep = used between the values. It defaults into a space character.
# end = After all values are printed, end is printed. It defaults into a new line.
# file = The file is the object where the values are printed and its default value is sys.stdout (screen).
# flush = https://stackoverflow.com/questions/15608229/what-does-prints-flush-do#:~:text=2%20Answers-,2,buffered%20goes%20to%20the%20destination.

#example
print(1, 2, 3, 4);
print(1, 2, 3, 4, sep='*');
print(1, 2, 3, 4, sep='#', end='&');

# Output format
# Sometimes we would like to format our output to make it look attractive. This can be done by using the str.format() method.

x = 5; y = 10;
print('The value of x is {} and y is {}'.format(x,y)); # use {} to output the content in format

# We can specify the order in which they are printed by using numbers (tuple index).
print('I love {0} and {1}'.format('bread','butter'));
print('I love {1} and {0}'.format('bread','butter'));

# Also
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

# Copy cat of C programming with sprintf()
x = 12.3456789
print('The value of x is %3.2f' %x);
print('The value of x is %3.4f' %x);



# Input

# Inputs provide dynamic values from users
num = input('Enter a number: ');
print(num);
print(type(num)); # these produce strings

# Convert inputs to int
print(type(int(num))); # there is also eval which will evaluate the content of the num https://towardsdatascience.com/python-eval-built-in-function-601f87db191#:~:text=Answer%3A%20eval%20is%20a%20built,the%20result%20as%20an%20integer.

