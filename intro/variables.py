import constants;

print("hello from python")

## --------------- Variables ---------------

# Avoid starting variables with _ unless python tells you too.
# Avoid differentiating variables with different cases. Ex: Spam, spam, SPAM.
# There is not really a way of creating constants but by declaring variables in a separate file and importing it to the main file.

hours = 35.0;
rate = 12.50;
pay = hours * rate;
print(pay);

website = "apple.com";
print(website);

# Note: Python is a type-inferred language, so you don't have to explicitly define the variable type. It automatically knows that apple.com is a string and declares the website variable as a string.


# Assign multiple values to multiple variables
a, b, c = 5, 3.2, "Hello";

print(a);
print(b);
print(c);

# Assign the same value to multiple variables
x = y = z = "same";

print(x);
print(x);
print(y);

# Using constants from the other module
print(constants.PI);
print(constants.GRAVITY);
 
## Literals - raw data given in a variable or constant. 

# Numerical -- Integer, Float and Complex

a = 0b1010; #Binary Literals
b = 100; #Decimal Literal 
c = 0o310; #Octal Literal
d = 0x12c; #Hexadecimal Literal

# Float Literal
float_1 = 10.5;
float_2 = 1.5e2;

# Complex Literal 
x = 3.14j;

print(a, b, c, d);
print(float_1, float_2);
print(x, x.imag, x.real);

# String & Character Literals
strings = "This is Python";
char = "C";

multiline_str = """This is a multiline 
string with more 
than one line code.""";

unicode = u"\u00dcnic\u00f6de";
raw_str = r"raw \n string"; # Raw string literals are string literals that are designed to make it easier to include nested characters like quotation marks and backslashes that normally have meanings as delimiters and escape sequence starts

print(strings);
print(char);
print(multiline_str);
print(unicode);
print(raw_str);

# Boolean Literal - True = 1 & False = 0
x = (1 == True);
y = (1 == False);
a = True + 4;
b = False + 10;

print("x is", x);
print("y is", y);
print("a:", a);
print("b:", b);

# Special Literals - None (nil in swift)
food = None; # null value or no value at all
print(food);

# Literal Collections - List, Tuple, Dict & Set
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple - they are immutable and ordered
alphabets = {'a':'apple','b':'ball','c':'cat'} #dictionary
vowels = {'a', 'e', 'i', 'o', 'u'} #set - cannot have multiple occurrences of the same element and store unordered values



