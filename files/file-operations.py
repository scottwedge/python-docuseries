## --------------- File I/O ---------------
#  file operation takes place in the following order:

# 1. Open a file
# 2. Read or write (perform operation)
# 3. Close the file

f = open('test.txt'); # default r

## File modes
# In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.
# The default is reading in text mode. In this mode, we get strings when reading from the file.
# Binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.
f = open("test.txt",'w');  # write in text mode
f = open("test.txt",'r+b'); # read and write in binary mode

# It is highly recommended to specify the encoding type
f = open("test.txt", mode='r', encoding='utf-8');

# When we are done with performing operations on the file, we clsoe it since a file will free up the resources that were tied with the file.\
f.close();

# The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.
# We don't need to explicitly call the close() method. It is done internally.

with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations
   pass;



## Write to files - overwrite content inside the file 
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n");
   f.write("This file\n\n");
   f.write("contains three lines\n");
   # This will create a new test.txt or overwrite the existing one

## Reading files
f = open("test.txt",'r',encoding = 'utf-8');
print(f.read(4)); # read the first 4 data
print(f.read(4)); # read the next 4 data
print(f.read());  # read in the rest till end of file
print(f.read());  # further reading returns empty string

print(f.tell()); # current position of cursor

print(f.seek(0)); # bring cursor to start
print(f.read())  # read the entire file

# We can also read the whole file line by line
for line in f:
     print(line, end = '');

# We can use the readline() method to read individual lines of a file.
print(f.seek(0)); # bring cursor to start
print(f.readline());
print(f.readline());
print(f.readline());
print(f.readline());