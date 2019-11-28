'''Sometimes you’ll need to recognize patterns in text, like phone
numbers, e-mail addresses, ZIP Codes, web page addresses,
Social Security numbers and more.'''
# importing regular expression library
import re

# REG EXPRESSION string describes a search pattern for matching chars
# in other strings

'''Regular expressions can help you extract data from unstructured 
text, such as social media posts. They’re also important for ensuring
that data is in the correct format before you attempt 
to process it.'''

# MATCHING LITERAL CHARACTERS
pattern = '02215'
print('Full Match: ')
print('Match' if re.fullmatch(pattern, '02215') else 'No match')
print('Match' if re.fullmatch(pattern, '51220') else 'No match')

print('Metacharacter Match with Character Classes: ')

''' RE \d{5}, \d is a character class representing a 
digit (0–9). A character class is a regular expression escape sequence
that matches one character. To match more than one, follow the 
character class with a quantifier. The quantifier {5} repeats \d 
five times, as if we had written \d\d\d\d\d, to match five 
consecutive digits'''

print("('Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid')")
print('Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid')
print('------------------------------------------------------------')

print("'Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid'")
print('Valid' if re.fullmatch(r'\d{5}', '9876') else 'Invalid')
print('-------------------------------------------------------------')


# OTHER PREDEFINED CHARACTER CLASSES
''' \d, \D, \s, \S, \w, \W are all predefined char classes '''


# CUSTOM CHARACTER CLASSES
'''Let’s validate a simple first name with no spaces or punctuation. 
We’ll ensure that it begins with an uppercase letter (A–Z) followed
by any number of lowercase letters (a–z)'''

print('Custom Character Classes')
print("'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid'")
print('-------------------------------------------------------------')

print("'Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid'")
print('Valid' if re.fullmatch('[A-Z][a-z]*', 'eva') else 'Invalid')
print('-------------------------------------------------------------')

'''[ABOVE] The * quantifier matches zero or more occurrences of the 
subexpression to its left (in this case, [a-z]). So [A-Z][a-z]* 
matches an uppercase letter followed by zero or more lowercase 
letters, such as 'Amanda', 'Bo' or even 'E'.'''

'''When a custom character class starts with a caret (^), the class 
matches any character that’s not specified. So [^a-z] matches any 
character that’s not a lowercase letter:'''

# Caret Character
print("'Match' if re.fullmatch('[^a-z]', 'A') else 'No match'")
print('Match' if re.fullmatch('[^a-z]', 'A') else 'No match')
print('-----------------------------------------------------')

print("'Match' if re.fullmatch('[^a-z]', 'a') else 'No match'")
print('Match' if re.fullmatch('[^a-z]', 'a') else 'No match')
print('-----------------------------------------------------')

# Literal Custom class Chars
'''Metacharacters in a custom character class are treated as literal 
characters—that is, the characters themselves. So [*+$] matches a 
single *, + or $ character:'''

print("'Match' if re.fullmatch('[*+$]', '*') else 'Not a match'")
print('Match' if re.fullmatch('[*+$]', '*') else 'Not a match')
print('----------------------------------------------------------')

print("'Match' if re.fullmatch('[*$+]', '!') else 'Not a match'")
print('Match' if re.fullmatch('[*$+]', '!') else 'Not a match')
print('---------------------------------------------------------')


# * vs + Quantifer
'''If you want to require at least one lowercase letter in a first 
name, you can replace the * quantifier in snippet [7] with +, which 
matches at least one occurrence of a subexpression:'''

print("'Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Not Valid'")
print('Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Not Valid')
print('-----------------------------------------------------------')

print("'Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Not Valid'")
print('Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Not Valid')
print('============================================================')


# OTHER QUANTIFIERS
'''? quantifier matches zero or one occurrences of a subexpression'''

print("'Match' if re.fullmatch('labell?ed', 'labelled') else 'No Match'")
print('Match' if re.fullmatch('labell?ed', 'labelled') else 'No Match')
print('-----------------------------------------------------------')

print("'Match' if re.fullmatch('labell?ed', 'labeled') else 'No match'")
print('Match' if re.fullmatch('labell?ed', 'labeled') else 'No match')
print('-----------------------------------------------------------')

print("'Match' if re.fullmatch('labell?ed', 'labellled') else 'No match'")
print('Match' if re.fullmatch('labell?ed', 'labellled') else 'No match')


'''You can match at least n occurrences of a subexpression with the 
{n,} quantifier. The following regular expression matches strings 
containing at least three digits:'''

print("'Match' if re.fullmatch(r'\d{3,}', '123') else 'No match'")
print('Match' if re.fullmatch(r'\d{3,}', '123') else 'No match')
print('----------------------------------------------')

print("'Match' if re.fullmatch(r'\d{3,}', '1234567890') else 'No match'")
print('Match' if re.fullmatch(r'\d{3,}', '1234567890') else 'No match')
print('=-===========================================================')

print("'Match' if re.fullmatch(r'\d{3,}', '12') else 'No match'")
print('Match' if re.fullmatch(r'\d{3,}', '12') else 'No match')
print('--------------------------------------------------------')

'''You can match between n and m (inclusive) occurrences of a 
subexpression with the {n,m} quantifier. The following regular 
expression matches strings containing 3 to 6 digits:'''

print("'Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match'")
print('Match' if re.fullmatch(r'\d{3,6}', '123') else 'No match')
print('---------------------------------------------------------')

print("'Match' if re.fullmatch(r'\d{3,6}', '123456') else 'No match'")
print('Match' if re.fullmatch(r'\d{3,6}', '123456') else 'No match')
print('===========================================================')

print("'Match' if re.fullmatch(r'\d{3, 6}', '1234567') else 'No match'")
print('Match' if re.fullmatch(r'\d{3, 6}', '1234567') else 'No match')
print('============================================================')

print("'Match' if re.fullmatch(r'\d{3, 6}', '12') else 'No match'")
print('Match' if re.fullmatch(r'\d{3, 6}', '12') else 'No match')
print('---------------------------------------------------------')




