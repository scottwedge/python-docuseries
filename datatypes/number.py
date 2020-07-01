## --------------- Numbers ---------------
import decimal;
import fractions;
import math;
import random;

a = 5; # int class
print(type(a));
b = 5.0; # float class , accurate up to 15 decimal places
print(type(b));

c = 5 + 3j # complex class
print(c + 3);
print(isinstance(c, complex));

## Number System

# Binary = 0b or 0B
# Octal = 0o or 0O
# Hexadecimal 0x or 0X

# Output: 107
print(0b1101011);

# Output: 253 (251 + 2)
print(0xFB + 0b10);

# Output: 13
print(0o15);



## Type conversion - coercion

# implicit
print(1 + 2.0) # 3.0 - here we have int being converted implicitly to float

# explicit - int(), float(), complex() - these functions can even be convert strings
int(2.3);
int(-2.8);
float(5);
complex('3+5j');


## Python Decimal
# Limitations since most of the decimal fractions we know, cannot be accurately stored in our computer.
# Decimal module has user-settable precision

print(0.1);
print(decimal.Decimal(0.1));


## Python Fractions
# A fraction has a numerator and a denominator, both of which are integers. This module has support for rational number arithmetic.

print(fractions.Fraction(1.5));

print(fractions.Fraction(5));

print(fractions.Fraction(1,3));

# While creating Fraction from float, we might get some unusual results. This is due to the imperfect binary floating point number representation as discussed in the previous section.
# Fortunately, Fraction allows us to instantiate with string as well. This is the preferred option when using decimal numbers.

# As float
# Output: 2476979795053773/2251799813685248
print(fractions.Fraction(1.1));

# As string
# Output: 11/10
print(fractions.Fraction('1.1'));

# This data type supports all basic operations


## Python Mathematics

print(math.pi);

print(math.cos(math.pi));

print(math.exp(10));

print(math.log10(1000));

print(math.sinh(1));

print(math.factorial(6));

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())
