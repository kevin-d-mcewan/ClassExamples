import re

'''Earlier we used the fullmatch function to determine whether an 
entire string matched a regular expression. There are several other 
searching functions. Here, we discuss the search, match, findall and 
finditer functions, and show how to access the matching substrings.'''

'''Function search looks in a string for the first occurrence of a 
substring that matches a regular expression and returns a match 
object (of type SRE_Match) that contains the matching substring.'''

result = re.search('Python', 'Python is fun')
print("result = re.search('Python', 'Python is fun')")
print(result.group() if result else 'not found')
print('------------------------------------------------')

result2 = re.search('fun!', 'Python is fun')
print("result2 = re.search('fun!', 'Python is fun')")
print(result2.group() if result2 else 'not found')
print('--------------------------------------------')
'''YOU CAN SEARCH FOR MATCH AT BEGINNING ONLY WITH FX MATCH'''

# IGNORING CASE WITH THE OPTIONAL flags KEYWORD ARGS
'''Many re module functions receive an optional flags keyword 
argument that changes how regular expressions are matched. For 
example, matches are case sensitive by default, but by using the 
re module’s IGNORECASE constant, you can perform a 
case-insensitive searc'''

print("result3 = re.search('Sam', 'SAM WHITE', flags = re.IGNORECASE)")
result3 = re.search('Sam', 'SAM WHITE', flags = re.IGNORECASE)
print(result3.group() if result3 else 'Not found')
print('--------------------------------------------------------')

# METACHARS THAT RESTRICT MATCHES TO BEG OR END OF STR
'''The ^ metacharacter at the beginning of a regular expression 
(and not inside square brackets) is an anchor indicating that the 
expression matches only the beginning of a string'''
print("result4 = re.search('^Python', 'Python is fun')")
result4 = re.search('^Python', 'Python is fun')
print(result4.group() if result4 else 'Not found\n')
print('-------------------------------------------')

print("result4 = re.search('^fun', 'Python is fun')")
result4 = re.search('^fun', 'Python is fun')
print(result4.group() if result4 else 'Not found')
print('-----------------------------------------------')

'''$ metacharacter at the end of a regular expression is an anchor 
indicating that the expression matches only the end of a string:'''

print("result = re.search('Python$', 'Python is fun')")
result = re.search('Python$', 'Python is fun')
print(result.group() if result else 'Not found')
print('----------------------------------------')

print("result = re.search('fun$', 'Python is fun')")
result = re.search('fun$', 'Python is fun')
print(result.group() if result else 'Not found')
print('================================================')


# Fx findall AND finditer - FINDING ALL MATCHES IN STRING
'''Function findall finds every matching substring in a string and 
returns a list of the matching substrings'''

'''Let’s extract all the U.S. phone numbers from a string. For 
simplicity we’ll assume that U.S. phone numbers 
have the form ###-###-####:'''

contact = 'Wally White, Home: 555-555-2345, Work: 555-555-4321'
print("contact = 'Wally White, Home: 555-555-2345, Work: 555-555-4321'")
print("re.findall(r'\d{3}-\d{3}-\d{4}', contact")
print(re.findall(r'\d{3}-\d{3}-\d{4}', contact))
print('--------------------------------------------')


# CAPTURING SUBSTRINGS IN A MATCH
'''parentheses metacharacters—( and )—to capture substrings in a match'''
text = 'Charlie Cyan, e-mail: demo1@deitel.com'
pattern = r'([A-Z][a-z]+  [A-Z][a-z]+), e-mail: (\w+@\w\.\w{3})'
result = re.search(pattern, text)

result.group()







