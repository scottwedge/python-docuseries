## --------------- Directory ---------------
# Python has the os module that provides us with many useful methods to work with directories
import os;
import shutil; # module that allows you to remove non-empty directories

print(os.getcwd());
print(os.getcwdb()); # get it as bytes object.

# Change the current directory
# os.chdir('C:\\Python33');

# All files and sub-directories inside a directory can be retrieved using the listdir()
print(os.listdir());

# Making a new directory
# os.mkdir('test');

# Renaming a directory
# os.rename('test','new_one');

# Removing a directory or file
# os.remove('old.txt');
# os.rmdir('new_one'); # The rmdir() method can only remove empty directories.

# In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module.
# shutil.rmtree('test');




