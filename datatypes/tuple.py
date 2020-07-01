## --------------- Tuple ---------------
# In short, it is an immutable list

# Empty tuple
my_tuple = ();
print(my_tuple);

# Tuple having integers 
my_tuple2 = (1, 2, 3);
print(my_tuple2);

# Tuple with mixed datatypes 
my_tuple3 = (1, 'Hello', 3.4);
print(my_tuple3);

# Nested tuple
my_tuple4 = ('mouse', [5,3,5], (1,2,3));
print(my_tuple4);


# Tuple packing
my_tuple5 = 3, 4.6, 'dog';
print(my_tuple5);

# Tuple unpacking
a, b, c = my_tuple5;
print(a);
print(b);
print(c);

# Tuple confusion
my_tuple6 = ('Hello'); # yields a string
print(type(my_tuple6));

# Tuple with one element is actually created by
my_tuple7 = ('Hello',); # adding a coma
print(type(my_tuple7))  # <class 'tuple'>

# Parentheses is optional
my_tuple8 = "hello",
print(type(my_tuple8))  # <class 'tuple'>



## Access tuple elements
#Indexing - Negative Indexing
my_tuple9 = ('p','e','r','m','i','t');
print(my_tuple9[5]);
# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3));
# nested index
print(n_tuple[0][3]);
# negative indexing
print(my_tuple9[-1]);

## Tuples can be reassigned
# Slicing works like with arrays
# If you have a list in a tuple, it can be changed
my_tuple = (4, 2, 3, [6, 5]);
my_tuple[3][0] = 9;
print(my_tuple);
# We can also concat and repeat a tuple like with lists
# Del works the same


# Methods that add items or remove items are not available with tuple. Only the following two methods are available.
my_tuple = ('a', 'p', 'p', 'l', 'e',);

print(my_tuple.count('p'));  # Output: 2
print(my_tuple.index('l'));  # Output: 3

# Tuple membership test and iteration is the same as list

## Why use tuples instead of lists
# 1. We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# 2. Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
# 3. Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# 4. If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

