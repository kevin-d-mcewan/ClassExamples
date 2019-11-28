#When you read a sentence, your brain breaks it into individual words, or tokens
# Interpreters tokenize statements breaking them into ind. componenets such
# as KEYWORDS, IDENTIFIERS, OPERATORS and OTHER ELEMENTS
''' Tokens typically are separated by whitespace characters such as
blank, tab and newline, though other characters may be used—the
separators are known as delimiters.'''

# SPLITING STRINGS
'''To tokenize a string at a custom delimiter (such as each 
comma-and-space pair), specify the delimiter string (such as, ', ') 
that split uses to tokenize the string:'''
letters = 'A, B, C, D'
print(letters.split(","))

#2nd ARG specifies max # of splits
print(letters.split(', ', 2))
'''RSPLIT method performs the same task as SPLIT but processes the 
max number of splits from end to beg'''

# JOINING STRINGS
'''join concatenates the strings in its argument, which must be an 
iterable containing only string values; otherwise, 
a TypeError occurs'''

letters_list = ['A', 'B', 'C', 'D']
print(','.join(letters_list))

'''Next line JOINS the results of a list comprehension that
creates a list of strings:'''
print(','.join([str(i) for i in range(10)]))


# STRING METHODS partition AND rpartition
'''PARTITION splits a string into a tuple of 3 strings based on the
method's separator args'''
'''3 strings are: 1.) The part of the og string b4 the separator
2.) The separator itself and 3.) The part of the string after
the separator'''
'''might be useful for splitting more complex strings.'''

'Amanda: 89, 97, 92'
print('Amanda: 89, 97, 93'.partition(': '))
print('-------------------------------')

''' RPARTITION starts from end works to beginning of string. So the
first / is where the SEPARATOR is '''
url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'
rest_of_url, separator, document = url.rpartition('/')
print('document variable is: ', document)
print('rest_of_url VAR is: ', rest_of_url)
print('separator is: ', separator)
print('-------------------------------------')

# STRING METHOD splitlines
'''If you read large amounts of text into a string, you might want to 
split the string into a list of lines based on newline characters. '''

'''Method SPLITLINES returns a list of new strings representing the 
lines of text split at each newline character in the original string'''

lines = """This is line 1
This is line2
This is line3"""

print(lines)
print(lines.splitlines())
print(lines.splitlines(True))
print('-----------------------------------')


