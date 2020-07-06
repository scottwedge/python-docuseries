## --------------- Regex ---------------
# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.

import re; # python regex library

pattern = '^a...s$'; # any five letter string starting with a and ending with s.
test_string = 'abyss';

result = re.match(pattern, test_string);

if result:
  print("Search successful.");
else:
  print("Search unsuccessful.");	


## Metacharacters
# Metacharacters are characters that are interpreted in a special way by a RegEx engine
# [] . ^ $ * + ? {} () \ |

# LEARN all about regex here 
# https://www.programiz.com/python-programming/regex