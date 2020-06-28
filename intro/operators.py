## --------------- Operators ---------------

# Arithmetic Operators

x = 15;
y = 4;

# Output: x + y = 19
print('x + y =',x+y);

# Output: x - y = 11
print('x - y =',x-y);

# Output: x * y = 60
print('x * y =',x*y);

# Output: x / y = 3.75
print('x / y =',x/y);

# Output: x // y = 3
print('x // y =',x//y); # Floor division - division that results into whole number adjusted to the left in the number line.

# Output: x ** y = 50625
print('x ** y =',x**y);



# Comparison Operators - return true or false

x = 10;
y = 12;

# Output: x > y is False
print('x > y is',x>y);

# Output: x < y is True
print('x < y is',x<y);

# Output: x == y is False
print('x == y is',x==y);

# Output: x != y is True
print('x != y is',x!=y);

# Output: x >= y is False
print('x >= y is',x>=y);

# Output: x <= y is True
print('x <= y is',x<=y);



# Logical Operators - return true or false

x = True;
y = False;

print('x and y is',x and y);

print('x or y is',x or y);

print('not x is',not x);



# Special operators = Identity operators & Membership operators

# Identity operators
# They are used to check if two values (or variables) are located on the same part of the memory

# is = returns True if the type of the value in the right operand points to the same type in the left operand. For example, type(3) is int evaluates to True because 3 is indeed an integer number.
# is not = returns True if the type of the value in the right operand points to a different type than the value in the left operand. For example, type(3) is not float: evaluates to True because 3 is not a floating-point value.

x1 = 5;
y1 = 5;
x2 = 'Hello';
y2 = 'Hello';
x3 = [1,2,3];
y3 = [1,2,3];

# Output: False
print(x1 is not y1);

# Output: True
print(x2 is y2);

# Output: False
print(x3 is y3);

# Here, we see that x1 and y1 are integers of the same values, so they are equal as well as identical. Same is the case with x2 and y2 (strings).
# But x3 and y3 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.

# Membership operators
#  They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

# in = True if value/variable is found in the sequence
# not in =	True if value/variable is not found in the sequence

x = 'Hello world';
y = {1:'a',2:'b'};

# Output: True
print('H' in x);

# Output: True
print('hello' not in x); # cause of the capital in x

# Output: True
print(1 in y); # only look at keys

# Output: False
print('a' in y);