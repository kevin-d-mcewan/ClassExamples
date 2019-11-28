# 8.12.2 REPLACING SUBSTRINGS AND SPLITTING STRINGS
'''The re module provides function sub for replacing patterns in a
string, and function split for breaking a string into pieces,
based on patterns.'''

import re

# FUNCTION sub - REPLACING PATTERNS
'''By default, the re module’s sub function replaces all occurrences 
of a pattern with the replacement text you specify. Let’s convert 
a tab-delimited string to comma-delimited'''

print("re.sub(r'\t', ', ', '1\t2\t3\t4')")
print(re.sub(r'\t', ', ', '1\t2\t3\t4'))
print('---------------------------------------------')

''' SUB fx receives 3 args: 1) pattern to match (tab char "\t", 
2) replacement text (', ') and 3) the string to be searched
("1\t2\t3\t4") '''

# COUNT can be used to specify max num of replacements
print("re.sub(r'\t', ', ', '1\t2\t3\t4', count = 2)")
print(re.sub(r'\t', ', ', '1\t2\t3\t4', count = 2))
print('----------------------------------------------------')

# FUNCTION SPLIT
'''The split function tokenizes a string, using a regular expression 
to specify the delimiter, and returns a list of strings'''

'''okenize a string by splitting it at any comma that’s followed by 
0 or more whitespace characters—\s is the whitespace character class
and * indicates zero or more occurrences of the preceding 
subexpression'''

print("re.split(r',\s*', '1,  2,  3,4,    5,6,7,8')")
print(re.split(r',\s*', '1,  2,  3,4,    5,6,7,8'))
print('-============================================')

'''keyword argument maxsplit to specify the maximum number of splits'''
print("re.split(r',\s*', '1,  2,  3,4,     5,6,7,8', maxsplit = 3)")
print(re.split(r',\s*', '1,  2,  3,4,     5,6,7,8', maxsplit = 3))
print('----------------------------------------------------------')
















