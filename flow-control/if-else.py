## --------------- If-else ---------------

# In Python, the body of the if statement is indicated by the indentation. The body starts with an indentation and the first unindented line marks the end.
# Python interprets non-zero values as True. None and 0 are interpreted as False.

num = 3;
if num > 0:
      print(num, "is a positive number.");
print("This is always printed.");

num = -1
if num > 0:
      print(num, "is a positive number.");
print("This is also always printed.");

# if-else
if num:
      print(num, " is always considered as true in python since it is not 0 or none");
else: 
      print("This has to be 0 or none");

# if...elif...else
num = 3.4

if num > 0:
    print("Positive number");
elif num == 0:
    print("Zero");
else:
    print("Negative number");

# nested if statements
# They can get confusing, so they must be avoided unless necessary.

num = float(input("Enter a number: "));

if num >= 0:
    if num == 0:
        print("Zero");
    else:
        print("Positive number");
else:
    print("Negative number");
