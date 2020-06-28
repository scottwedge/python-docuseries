## --------------- Data Types ---------------

# Everything is an object in python
# Data types are usually classes and variables are instance (object) of these classes



# Numbers: Int, Float and Complex

a = 5;
print(a, "is of type", type(a));

a = 2.0;
print(a, "is of type", type(a));

a = 1+2j;
print(a, "is complex number?", isinstance(a,complex));

# Long floats can get truncated ex: input --> 0.1234567890123456789 , output --> 0.12345678901234568



# List: ordered sequence of items

a = [5,10,15,20,25,30,35,40];

# a[2] = 15
print("a[2] = ", a[2]);

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3]); # range

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:]); # range

# Tuple: ordered sequence of items & tuples are immutable.

t = (5,'program', 1+3j);

# t[1] = 'program'
print("t[1] = ", t[1]);

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3]);

# Generates error
# Tuples are immutable
# t[0] = 10; <-- cannot be done

# Set: unordered collection of UNIQUE items.
# Since, set are unordered collection, indexing has no meaning

a = {5,2,3,1,4};

# printing set variable
print("a = ", a);

# data type of variable a
print(type(a));




# Strings: sequence of Unicode characters, strings are IMMUTABLE
# We can use single quotes, double quotes & triple quotes (multi line) to represent strings

# Regular
s = "This is a string";
print(s);

# Tripple quotes
s = '''A multiline
string''';
print(s);

# Can be treated as arrays
s = 'Hello world!';

# s[4] = 'o'
print("s[4] = ", s[4]);

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11]);

# Generates error
# Strings are immutable in Python
# s[5] ='d' <-- cannot be done


# Dictionary: unordered collection of key-value pairs.
# Used when we have a huge amount of data

d = {1: 'value', 'key': 2};
print(type(d))

print("d[1] = ", d[1]); # this is a key
print("d['key'] = ", d['key']); # this is a key
# Generates error
print("d[2] = ", d[2]); # this is not a key
