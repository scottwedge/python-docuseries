## --------------- Dictionary ---------------
# Dictionaries are optimized to retrieve values when the key is known.

# empty dictionary
my_dict = {};

my_dict = {'name': 'John', 1: [2, 4, 3]};

my_dict = dict({1:'apple', 2:'ball'});

# As you can see from above, we can also create a dictionary using the built-in dict() function.

# # get vs [] for retrieving elements
my_dict = {'name': 'Jack', 'age': 26};

# []
print(my_dict['name']);

# get
print(my_dict.get('age'));

# If we use the square brackets [], KeyError is raised in case a key is not found in the dictionary. On the other hand, the get() method returns None if the key is not found.

# add & update

# update value
my_dict['age'] = 27;

# add item
my_dict['address'] = 'Downtown'

# removing

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25};

# remove a particular item, returns its value
print(squares.pop(4));

# remove an arbitrary item, return (key,value)
print(squares.popitem());

# remove all items
squares.clear();


# Creating a new dict called marks with default vals of 0
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks);

for item in marks.items():
    print(item);


# Dictionary comprehension
squares = {x: x*x for x in range(6)};

print(squares);


# Membership Test - tests only keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81};

# Output: True
print(1 in squares);

# Output: True
print(2 not in squares);