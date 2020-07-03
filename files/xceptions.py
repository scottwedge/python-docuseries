## --------------- Exception ---------------
# A python program terminates as soon as it encounters an unhandled error. 
# These errors can be broadly classified into two classes

# 1. Syntax errors
# 2. Logical errors (Exceptions)

## Syntax error
# if a < 3
#  File "<interactive input>", line 1
#    if a < 3
#           ^
# SyntaxError: invalid syntax

## Logical error (called exceptions) , these occur at run time
# Whenever these types of runtime errors occur, Python creates an exception object. If not handled properly, it prints a traceback to that error along with some details about why that error occurred.

# List of all exceptions
# https://docs.python.org/3/library/exceptions.html

# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# For example, let us consider a program where we have a function A that calls function B, which in turn calls function C. If an exception occurs in function C but is not handled in C, the exception passes to B and then to A.

# If never handled, an error message is displayed and our program comes to a sudden unexpected halt.

# Catching exceptions
# The critical operation which can raise an exception is placed inside the try clause. The code that handles the exceptions is written in the except clause.
import sys; # import module sys to get the type of exception

randomList = ['a', 0, 2];

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break;
    except:
        print("Oops!", sys.exc_info()[0], "occurred."); # Here, we print the name of the exception using the exc_info() function inside sys module.
        print("Next entry.");
        print();

print("The reciprocal of", entry, "is", r);




# Since every exception in Python inherits from the base Exception class, we can also perform the above task in the following way:
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e: # <-- here base Exception class
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)




# We can also catch specific exceptions
try:
   # do something
   pass;

except ValueError:
   # handle ValueError exception
   pass;

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass;

except:
   # handle all other exceptions
   pass;




# Raise exceptions in Python
try:
      a = int(input("Enter a positive integer: "));
      if a <= 0:
            raise ValueError("That is not a positive number!"); # <-- raise this error and pass the reason as argument
except ValueError as ve:
      print(ve);



# In some situations, you might want to run a certain block of code if the code block inside try ran without any errors.
try:
    num = int(input("Enter a number: "));
    assert num % 2 == 0; # The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
except:
    print("Not an even number!");
else:
    reciprocal = 1/num;
    print(reciprocal);



# Finally clause
# This clause is executed no matter what, and is generally used to release external resources.
try:
   f = open("test.txt",encoding = 'utf-8');
   # perform file operations
finally:
   f.close();






## Creating Custom Exceptions
# In Python, users can define custom exceptions by creating a new class.
class CustomError(Exception):
    pass;

# When we are developing a large Python program, it is a good practice to place all the user-defined exceptions that our program raises in a separate file. Many standard modules do this. They define their exceptions separately as exceptions.py or errors.py

# Customizing Exception Classes
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary;
        self.message = message;
        super().__init__(self.message);


salary = int(input("Enter salary amount: "));
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary);


