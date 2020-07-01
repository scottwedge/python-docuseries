## --------------- List ---------------
# List is one of the most frequently used and very versatile data types used in Python.

# empty list
my_list = [];

# list of integers
my_list = [1, 2, 3];

# list with mixed data types
my_list = [1, "Hello", 3.4];

# nested list
my_list = ["mouse", [8,4,3], ['a']];

## Access elements from a list
my_list = ['p', 'r', 'o', 'b', 'e'];

# Output: p
print(my_list[0]);

# Output: o
print(my_list[2]);

# Output: e
print(my_list[4]);

# Nested List
n_list = ["Happy", [2, 0, 1, 5]];

# Nested indexing
print(n_list[0][1]);

print(n_list[1][3]);

# Error! Only integer can be used for indexing
# print(my_list[4.0]);



# Negative indexing in lists
my_list = ['p','r','o','b','e'];

print(my_list[-1]);

print(my_list[-5]);



# List slicing in Python
my_list = ['p','r','o','g','r','a','m','i','z'];

# elements 3rd to 5th
print(my_list[2:5]);

# elements beginning to 4th
print(my_list[:-5]);

# elements 6th to end
print(my_list[5:]);

# elements beginning to end
print(my_list[:]);



# Change elements to a list
# Correcting mistake values in a list
odd = [2, 4, 6, 8];

# change the 1st item    
odd[0] = 1;         

print(odd);

# change 2nd to 4th items
odd[1:4] = [3, 5, 7];

print(odd);     



# Add elements to a list
# Appending and Extending lists in Python
odd = [1, 3, 5];

odd.append(7);

print(odd);

odd.extend([9, 11, 13]);

print(odd);



# Concat two lists
# Concatenating and repeating lists
odd = [1, 3, 5];

print(odd + [9, 7, 5]);




# Repeat list - produces one of array or r3 3 times
print(["re"] * 3);


# Insert @ specific location
# Demonstration of list insert() method
odd = [1, 9];
odd.insert(1,3);

print(odd);

odd[2:2] = [5, 7];

print(odd);



# Delete or remove elements from a list
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']

# delete one item
del my_list[2];

print(my_list);

# delete multiple items
del my_list[1:5];

print(my_list);

# delete entire list
del my_list;

# Error: List not defined
# print(my_list);

my_list = ['p','r','o','b','l','e','m'];
my_list.remove('p');

# Output: ['r', 'o', 'b', 'l', 'e', 'm']
print(my_list);

# Output: 'o'
print(my_list.pop(1));

# Output: ['r', 'b', 'l', 'e', 'm']
print(my_list);

# Output: 'm'
print(my_list.pop()); # last element

# Output: ['r', 'b', 'l', 'e']
print(my_list);

my_list.clear();

# Output: []
print(my_list);



## List methods examples
# Python list methods
my_list = [3, 8, 1, 6, 0, 8, 4];

# Output: 1
print(my_list.index(8));

# Output: 2
print(my_list.count(8));

my_list.sort();

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list);

my_list.reverse();

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list);





## Elegant way to create new List
# List comprehension CREATES list in elegant way
# Consists of an expression followed by for statement inside square brackets.
pow2 = [2 ** x for x in range(10)]; # 2 power of 1,2,3,4,5,6,7,8,9,10
print(pow2);

# A list comprehension can optionally contain more for or if statements.
pow2 = [2 ** x for x in range(10) if x > 5];
odd = [x for x in range(20) if x % 2 == 1];
# Distribution
[x+y for x in ['Python ','C '] for y in ['Language','Programming']];




## List Membership Test
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm'];

# Output: True
print('p' in my_list);

# Output: False
print('a' in my_list);

# Output: True
print('c' not in my_list);




## Iteration Through a List
for fruit in ['apple','banana','mango']:
    print("I like",fruit);