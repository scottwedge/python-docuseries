## --------------- OOP ---------------
# The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

## Class - attributes, methods and initializers
class Parrot:
      '''This is a docstring. I have created a new class'''

      # class attribute
      species = "bird";

      # instance attribute
      def __init__(self, name, age):
            self.name = name;
            self.age = age;

      # instance method
      def sing(self, song):
            return "{} sings {}".format(self.name, song);

      def dance(self):
            return "{} is now dancing".format(self.name);

# instantiate the object
blu = Parrot("Blu", 10);

# call our instance methods
print(blu.sing("'Happy'"));
print(blu.dance());


## Inheritance
# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready");

    def whoisThis(self):
        print("Bird");

    def swim(self):
        print("Swim faster");

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__();
        print("Penguin is ready");

    def whoisThis(self): # Method overriding
        print("Penguin");

    def run(self):
        print("Run faster");

peggy = Penguin();
peggy.whoisThis();
peggy.swim();
peggy.run();


## Encapsulation
# We can restrict access to methods and variables.
# This prevents data from direct modification which is called encapsulation.
class Computer:

    def __init__(self):
        self.__maxprice = 900; # private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice));

    def setMaxPrice(self, price):
        self.__maxprice = price;

c = Computer();
c.sell(); # check value

# change the price
c.__maxprice = 1000; # neglect modification
c.sell();

# using setter function
c.setMaxPrice(1000); # can modify
c.sell();



# Polymorphsim
## Use a common interface for multiple forms 

class Parrot:

    def fly(self):
        print("Parrot can fly");
    
    def swim(self):
        print("Parrot can't swim");

class Penguin:

    def fly(self):
        print("Penguin can't fly");
    
    def swim(self):
        print("Penguin can swim");

# common interface
def flying_test(bird): # will use same method for both data types
    bird.fly();

#instantiate objects
blu = Parrot();
peggy = Penguin();

# passing the object
flying_test(blu);
flying_test(peggy);




## Deleting objects and arguments
# Any attribute of an object can be deleted anytime, using the del statement
# We can even delete the object itself, using the del statement.




## Multiple Inheritance
# A class can be derived from more than one base class in Python, CANNOT BE DONE IN JAVA
class Base1:
    pass;

class Base2:
    pass;

class MultiDerived(Base1, Base2):
    pass;



## Python Multilevel Inheritance
class Base:
    pass;

class Derived1(Base):
    pass;

class Derived2(Derived1):
    pass;



## Method Resolution Order in Python
# Every class in Python is derived from the object class. It is the most base type in Python.

# Output: True
print(issubclass(list,object));

# Output: True
print(isinstance(5.5,object));

# Output: True
print(isinstance("Hello",object));

# Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes
# Demonstration of MRO

class X:
    pass;


class Y:
    pass;


class Z:
    pass;


class A(X, Y):
    pass;


class B(Y, Z):
    pass;


class M(B, A, Z):
    pass;

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
#  <class '__main__.A'>, <class '__main__.X'>,
#  <class '__main__.Y'>, <class '__main__.Z'>,
#  <class 'object'>]

print(M.mro());



## Python Operator Overloading
# You can change the meaning of an operator in Python depending upon the operands used.

class Point:
      def __init__(self, x=0, y=0):
            self.x = x;
            self.y = y;

      def __str__(self): # modify the print function for this class
            return "({0},{1})".format(self.x,self.y);

      def __add__(self, other): # overload the + operator
            x = self.x + other.x;
            y = self.y + other.y;
            return Point(x, y);


p1 = Point(1, 2);
p2 = Point(2, 3);
# print(p1+p2) <-- Python won't recognize how to do this. Unless we modify the __add__ method. 

# However, we can achieve this task in Python through operator overloading. But first, let's get a notion about special functions.

# Class functions that begin with double underscore __ are called special functions in Python. 
# https://docs.python.org/3/reference/datamodel.html#special-method-names

# To overload the + operator, we will need to implement __add__() function in the class.

print(p1+p2); # Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2)

# Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.
