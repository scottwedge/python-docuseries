## --------------- String ---------------
# Character to a number is called encoding. (ASCII and Unicode are some of the popular encodings used.)
# In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding.
# Strings are immutable so changing individual characters is not possible

# defining strings in Python
# all of the following are equivalent
my_string = 'Hello';
print(my_string);

my_string = "Hello";
print(my_string);

my_string = '''Hello''';
print(my_string);

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python""";
print(my_string);

# Access characters in a string with indexing
str = 'programiz';
print('str[0] = ', str[0]);
# You can even slice
print('str[1:5] = ', str[1:5]);


# Concat strings
str1 = 'Hello';
str2 ='World!';

# using +
print('str1 + str2 = ', str1 + str2);

# using *
print('str1 * 3 =', str1 * 3);



# Iterating through a string
count = 0;
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1;
print(count,'letters found');


# String membership is legal in strings
print('a' in 'program');
print('g' not in 'program');


# Built-in functions to work with Python
str = 'cold';

# enumerate()
list_enumerate = list(enumerate(str));
print('list(enumerate(str) = ', list_enumerate);

#character count
print('len(str) = ', len(str));



# String formatting
# An escape sequence starts with a backslash and is interpreted differently.
# using triple quotes
print('''He said, "What's there?"''');

# escaping single quotes
print('He said, "What\'s there?"');

# escaping double quotes
print("He said, \"What's there?\"");

# backslash
print("C:\\Python32\\Lib");

# new line
print("This is printed\nin two lines");

# hexadecimal
print("This is \x48\x45\x58 representation");

# ignor escape sequences with r in front
print(r"This is \x61 \ngood example");



# format()
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean');
print('\n--- Default Order ---');
print(default_order);

# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean');
print('\n--- Positional Order ---');
print(positional_order);

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean');
print('\n--- Keyword Order ---');
print(keyword_order);


# Common Python String Methods
print("PrOgRaMiZ".lower());
print("PrOgRaMiZ".upper());
print("This will split all words into a list".split());
print(' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string']));
print('Happy New Year'.find('ew'));
print('Happy New Year'.replace('Happy','Brilliant'));