'''Recall that backslash characters in strings introduce escape
sequences—like \n for newline and \t for tab. So, if you wish to
include a backslash in a string, you must use two back-slash
characters \\. This makes some strings difficult to read'''

# Rep a file location on windows write:
print('Non Raw String')
file_path = 'C:\\MyFolder\\MySubFolder\\MyFile.txt'
print(file_path)
print('==---------------------------------')
''' raw strings—preceded by the character r—are more convenient. 
They treat each backslash as a regular character, rather than the
 beginning of an escape sequence:'''

print('Raw String used')
file_path1 = r'C:\MyFolder\MySubFolder\MyFile.txt'
print(file_path1)


