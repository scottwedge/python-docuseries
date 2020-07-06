## --------------- Set ---------------
# A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# However, a set itself is mutable. We can add or remove items from it.
# Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

my_set = {1, 2, 3};
print(my_set);

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}; # A set cannot have mutable elements like lists, sets or dictionaries as its elements.
print(my_set);

# we can make set from a list
my_set = set([1, 2, 3, 2]);
print(my_set);

# Empty curly braces {} will make an empty dictionary in Python. To make a set without any elements, we use the set() function without any argument.
# initialize a with set()
a = set();


## Set operations
my_set = {1, 3};
print(my_set);

# Add a single element using the add() method
my_set.add(2);
print(my_set);

# Add multiple elements
my_set.update([4, 5], {1, 6, 8}); # The update() method can take tuples, lists, strings or other sets as its argument. In all cases, duplicates are avoided.
print(my_set);

# Discard element
my_set.discard(4);
print(my_set);

# Remove element
my_set.remove(6);
print(my_set);

# Discard vs Remove -> The only difference between the two is that the discard() function leaves a set unchanged if the element is not present in the set. On the other hand, the remove() function will raise an error in such a condition (if element is not present in the set).

# Remove and return an item
number = my_set.pop(); # Since set is an unordered data type, there is no way of determining which item will be popped. It is completely arbitrary.
print(number);
print(my_set);

# Remove all elements
my_set.clear();
print(my_set);



## Set operations

# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5};
B = {4, 5, 6, 7, 8};

# Union
print(A | B);
# or
print(A.union(B));
# or
print(B.union(A));

# Intersection
print(A & B);
# or
print(A.intersection(B));
# or
print(B.intersection(A));

# Difference
print(A - B);
print(B - A);
# or
print(A.difference(B));
# or
print(B.difference(A));

# Symmetric Difference
print(A ^ B);
# or
print(A.symmetric_difference(B));
# or
print(B.symmetric_difference(A));




# Membership Test
# in keyword in a set
# initialize my_set
my_set = set("apple");
# Check if 'a' is present
print('a' in my_set);
# Check if 'p' is present
print('p' not in my_set);



# Iterating Through a Set
for letter in set("apple"):
      print(letter);

# Sets have built-in functions
# Built-in functions like all(), any(), enumerate(), len(), max(), min(), sorted(), sum() etc. are commonly used with sets to perform different tasks.


## Frozen set
# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. While tuples are immutable lists, frozensets are immutable sets.

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4]);
B = frozenset([3, 4, 5, 6]);

# This data type supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union().