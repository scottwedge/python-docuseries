## --------------- Namespace & Scope ---------------

# introduction

# We can get the address (in RAM) of some object through the built-in function id()
a = 2; # 2 is stored at 9756224, which means a points to 9756224
print('id(a) =', id(a));

a = a+1; # since a = 3, this means that a becomes 3 and no points to 9756256
print('id(a) =', id(a)); #  9756256

print('id(3) =', id(3)); # 3 resides in  9756256 because of the above operation

b = 2; # 2 resides 9756224 because of the above operation
print('id(b) =', id(b)); # b points to 9756224
print('id(2) =', id(2)); # 9756224

# *NOTE your memory location will vary compared to mine

# This is efficient as Python does not have to create a new duplicate object. This dynamic nature of name binding makes Python powerful; a name could refer to any type of object.

# These will yield 3 different ID's/RAM locations
a = 5;
print('5 --> id(a) =', id(a));
a = 'Hello World!';
print('Hello World! --> id(a) =', id(a));
a = [1,2,3];
print('[1,2,3] --> id(a) =', id(a));

# The same we can od if we do a = printHello() with a function


## What is a Namespace in Python?

# It is a system that ensures the names in a program are unique a can be used without any conflict
# Python implements namespaces as dictionaries
# In python every module, class and function have their own namespace. 

var_name = 7; # key, value => [(var_name, 7)] --> key is the name and value is the object

## Scopes in Python

# A scope is the portion of a program from where a namespace can be accessed directly without any prefix.

# 3 types of scopes:

# 1. Scope of the current function which has local names.
# 2. Scope of the module which has global names.
# 3. Outermost scope which has built-in names.


# When a reference is made inside a function, the name is searched in the local namespace, then in the global namespace and finally in the built-in namespace.

def outer_function():
    b = 20; # b is defined in the local namespace
    def inner_func():
        c = 30; # c is defined in the nested local namespace

a = 10; # a is defined in the global namespace

# An exmaple of a pertaining to different scopes and creating 3 different references
# In this program, three different variables a are defined in separate namespaces and accessed accordingly.

def outer_function():
    a = 20;

    def inner_function():
        a = 30;
        print('a =', a);

    inner_function();
    print('a =', a);


a = 10;
outer_function();
print('a =', a);

# While in the following program, all references and assignments are to the global a due to the use of keyword global.

def outer_function():
    global a;
    a = 20;

    def inner_function():
        global a;
        a = 30;
        print('a =', a);

    inner_function();
    print('a =', a);


a = 10;
outer_function();
print('a =', a);