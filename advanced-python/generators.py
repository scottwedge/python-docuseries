## --------------- Generators ---------------
# Python generators are a simple way of creating iterators
# Generators solve memory issues.Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time and neglects storing the entire sequence of numbers when we dont need to do that. 

#  It is as easy as defining a normal function, but with a yield statement instead of a return statement.
# If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function

# A simple generator function
def my_gen():
    n = 1;
    print('This is printed first');
    # Generator function contains yield statements
    yield n;

    n += 1
    print('This is printed second');
    yield n;

    n += 1
    print('This is printed at last');
    yield n;

# It returns an object but does not start execution immediately.
a = my_gen();

# We can iterate through the items using next().
next(a);

# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and theirs states are remembered between successive calls.
next(a);
next(a);

# There is a lot more about generators by this is simple a intro section in order to be aware about them. 