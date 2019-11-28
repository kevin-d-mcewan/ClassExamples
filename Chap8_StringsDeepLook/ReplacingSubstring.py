'''Method REPLACE takes two substrings. It searches a string for the
substring in its first argument and replaces EACH occurrence with the
substring in its second argument. The method returns a new string
containing the results'''

values = '1\t2\t3\t4\t6'
print(values)
print(values.replace('\t', ','))

# REPLACING can receive an optional third argument specifying in
# the maximum number of replacements to perform