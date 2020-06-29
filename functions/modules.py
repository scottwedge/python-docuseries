## --------------- Modules ---------------

# We use modules to break down large programs into small manageable and organized files. Furthermore, modules provide reusability of code.


# Import module
import example;

print(example.add(4,5.5));

# Python has tons of standard modules. You can check out the full list of Python standard modules and their use cases. https://docs.python.org/3/py-modindex.html 


# Import with renaming
import math as m;
print("The value of pi is", m.pi);

# *NOTE Note that the name math is not recognized in our scope. Hence, math.pi is invalid, and m.pi is the correct implementation.


# Import specific code
from math import pi, e;
print(pi);
print(e);


# Import all names
from math import * # Importing everything with the asterisk (*) symbol is not a good programming practice.
print("The value of pi is", pi)

# Here, we have imported all the definitions from the math module. This includes all names visible in our scope except those beginning with an underscore(private definitions).




## Python Module Search Path

# While importing a module, Python looks at several places. Interpreter first looks for a built-in module. Then(if built-in module not found), Python looks into a list of directories defined in sys.path. The search is in this order.

# 1. The current directory.
# 2. PYTHONPATH (an environment variable with a list of directories)
# 3. The installation-dependent default directory.



## The dir() built-in function
# We can use the dir() function to find out names that are defined inside a module.
print(dir(example)); 

# Underscore vars are default Python attributes associated with the module 
# Example

print(example.__name__);
print(example.__file__);

#  names defined in our current namespace
print(dir());