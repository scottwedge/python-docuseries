## --------------- Function ---------------

# Function

def greet(name):
      # Part of the Docstring
      """
      This function greets to
      the person passed in as
      a parameter
      """
      print("Hello, " + name + ". Good morning!");

# Calling function
greet('Paul');
# Check documentation of function
print(greet.__doc__);


# Function with return

def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num;
    else:
        return -num;


print(absolute_value(2));
print(absolute_value(-4));

# Scope and lifetime of variables
# The lifetime of variables inside a function is as long as the function executes.
# They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.

def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

## --------------- Function Arguments ---------------

def greet(name, msg): # two parameters 
      """ This function greets to
      the person with the provided message """
      print("Hello", name + ', ' + msg);

greet("Monica", "Good morning!");

# 3 Special python function definitions
# In Python, there are other ways to define a function that can take variable number of arguments.


# 1. Variable Function Arguments
# Function arguments can have default values in Python.
# We can provide a default value to an argument by using the assignment operator (=)

def greet(name, msg="Good morning!"): # 'name' does not have a default value and is required (mandatory) during a call.
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg); 


greet("Kate");
greet("Bruce", "How do you do?");


# NOT TO DO: 
# def greet(msg = "Good morning!", name): --> SyntaxError: non-default argument follows default argument
# Any number of arguments in a function can have a default value. But once we have a default argument, all the arguments to its right must also have default values.


# 2. Python Keyword Arguments
# Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?");

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") ;

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?");

# NOT TO DO: 
# greet(name="Bruce","How do you do?") --> SyntaxError: non-keyword arg after keyword arg
# We must keep in mind that keyword arguments must follow positional arguments


# 3. Python Arbitrary Arguments
# Sometimes, we do not know in advance the number of arguments that will be passed into a function.

def greet(*names): # asterisk is used to denote this arbitrary argument
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name);

# These arguments get wrapped up into a tuple before being passed into the function. 
greet("Monica", "Luke", "Steve", "John");



## --------------- Recursion ---------------
# The Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.
# By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError. Let's look at one such condition.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1; # Base condition
    else:
        return (x * factorial(x-1));


num = 3
print("The factorial of", num, "is", factorial(num));



## --------------- Anonymous Function ---------------
# Function that is defined without a name.
# Anonymous functions are defined using the lambda keyword.
# Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. 

# lambda arguments: expression
double = lambda x: x * 2;

print(double(5));

# In Python, we generally use it as an argument to a higher-order function = a function that takes in other functions as arguments

# Example use with filter()
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12];

new_list = list(filter(lambda x: (x%2 == 0) , my_list));

print(new_list);

# Example use with map()
# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12];

new_list = list(map(lambda x: x * 2 , my_list));

print(new_list);


## --------------- Function Scopes ---------------

#The basic rules for global keyword in Python are:
      #When we create a variable inside a function, it is local by default.
      #When we define a variable outside of a function, it is global by default. You don't have to use global keyword.
      #We use global keyword to read and write a global variable inside a function.
      #Use of global keyword outside a function has no effect.

c = 1; # global variable

def add():
    print(c); # accesses automatically global variable

add();


# Modifying Global Variable From Inside the Function
x = "global ";

def foo():
    global x; # reference global x before in order to use it
    y = "local";
    x = x * 2;
    print(x);
    print(y);

foo();

# In Python, we create a single module config.py to hold global variables and share information across Python modules within the same program.


# Using a Global variable in nested function
def foo():
    x = 20;

    def bar():
        global x;
        x = 25;
    
    print("Before calling bar: ", x);
    print("Calling bar now");
    bar();
    print("After calling bar: ", x);

foo();
print("x in main: ", x);

# Nonlocal Variables
# Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

def outer():
    x = "local"; # this one, is the actual variable being changed - only affect function scoped

    def inner():
        nonlocal x; # meaning that you aim for the var outside this function, inside the parent function. Having global here would look for outside x var
        x = "nonlocal";
        print("inner:", x);

    inner();
    print("outer:", x);

outer();