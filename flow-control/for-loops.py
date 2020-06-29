## --------------- For Loops ---------------

# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

# List
a = [5,10,15,20,25,30,35,40];
# iterate over the List
for val in a:
      print("List value", val);

# Set
b = {5,2,3,1,4};
# iterate over the Set
for val in b:
      print("List value", val);

# Tuple
c = (5,'program', 1+3j);
# iterate over the Tuple
for val in c:
      print("List value", val);

# Dictionary
d = {1: 'value', 'key': 2};
# iterate over the list
for key, value in d.items():
      print("key: ", key, "value: ", value);




## The range() function
# range(start, stop,step_size);

print(range(10)); # starts at 0

print(list(range(10)));

print(list(range(2, 8))); # exclusive the second arg

print(list(range(2, 20, 3)));

# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz'];

# iterate over the list using index
for i in range(len(genre)): # len is length of list, the ncreate range(3) --> 0,1,2
	print("I like", genre[i]);




## for loop with else
# A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.

digits = [0, 1, 5];

for i in digits:
    print(i);
else:
    print("No items left.");

# running else block only when the break keyword was not executed
student_name = 'James'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student]);
        break;
else:
    print('No entry with that name found.');