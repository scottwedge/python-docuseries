## --------------- Conversion ---------------

# The process of converting the value of one data type (integer, string, float, etc.) to another data type is called type conversion

# Python has two types of type conversion.
# 1. Implicit Type Conversion
# 2. Explicit Type Conversion



## Implicit Type Conversion
# In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

num_int = 123;
num_float = 1.23;

num_new = num_int + num_float;

print('datatype of num_int: ', type(num_int));
print('datatype of num_float: ', type(num_float));

print('Value of num_new: ', num_new);
print('datatype of num_new: ', type(num_new)); # yields a float

# Python always converts smaller data types to larger data types to avoid the loss of data.



## Explicit Type Conversion
# In Explicit Type Conversion, users convert the data type of an object to required data type

num_int = 123;
num_str = "456";

print("Data type of num_int:",type(num_int));
print("Data type of num_str before Type Casting:",type(num_str));

num_str = int(num_str);
print("Data type of num_str after Type Casting:",type(num_str));

num_sum = num_int + num_str;

print("Sum of num_int and num_str:",num_sum);
print("Data type of the sum:",type(num_sum));