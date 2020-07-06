## --------------- Iterators ---------------
# Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.
# Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol
# An object is called iterable if we can get an iterator from it

# define a list
my_list = [4, 7, 0, 3];

# get an iterator using iter()
my_iter = iter(my_list);

# iterate through it using next()

# Output: 4
print(next(my_iter));

# Output: 7
print(next(my_iter));

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__());

# Output: 3
print(my_iter.__next__());

# This will raise error, no items left, it will raise the StopIteration Exception
next(my_iter);


# We can take a look at how for loops are implemented in python
# create an iterator object from that iterable
iterable = [4, 7, 0, 3];

iter_obj = iter(iterable);

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break;


## Iterators from scratch
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max;

    def __iter__(self): # method overloading 
        self.n = 0;
        return self;

    def __next__(self): # method overloading 
        if self.n <= self.max:
            result = 2 ** self.n;
            self.n += 1;
            return result;
        else:
            raise StopIteration;


# create an object
numbers = PowTwo(3);

# create an iterable from the object
i = iter(numbers);

# Using next to get to the next iterator element
print(next(i));
print(next(i));
print(next(i));
print(next(i));
print(next(i));