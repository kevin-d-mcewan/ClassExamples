# COUNTING OCCURRENCES
sentence = 'to be or not to be that is the question'
'''If you specify as the second argument a start_index, count 
searches only the slice string[start_index:]—that is, from start_index
through end of the string:'''
print(sentence.count('to'))

'''If you specify as the second and third arguments the start_index 
and end_index, count searches only the slice string
[start_index:end_index]—that is, from start_index up to, but not 
including, end_index:'''
print(sentence.count('to', 12))

# LOCATING A SUBSTRING IN A STRING
'''String method index searches for a substring within a string and 
returns the first index at which the substring is found'''
print(sentence.index('be'))

'''String method rindex performs the same operation as index, but 
searches from the end of the string and returns the last index at 
which the substring is found'''
print(sentence.rindex('be'))
print('---------------------------------')
'''String methods find and rfind perform the same tasks as index and 
rindex but, if the substring is not found, return -1 rather than 
causing a Value-Error'''

# DETERMINING WHETHER A STRING CONTAINS A SUBSSTRINGS
'''Use "in" or "not in" to know whether a substring is in a string'''
print('that' in sentence)
print('THAT' in sentence)
print('THAT' not in sentence)
print('--------------------------------')
# LOCATING A SUBSTRING AT THE BEG OR END OF A STRING
'''String methods startswith and endswith return True if the string 
starts with or ends with a specified substring:'''

print(sentence.startswith('to'))
print(sentence.startswith('be'))
print(sentence.endswith('question'))
print(sentence.endswith('quest'))










