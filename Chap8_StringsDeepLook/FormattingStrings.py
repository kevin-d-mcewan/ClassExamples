from decimal import Decimal

# PRESENTATION TYPES
print(f'{17.489:.2f}')
print('-------------------')

# INTEGERS
'''The "d" PRESENTATION TYPE formats integer values as strings'''
print(f'Using Presentation Type to make an integer as a string:  \
      \n{10:d}')
'''PRESENTATION TYPE: (b, o, x or X) can be used to format integers 
(binary, octal or hexidecimal)'''
print('--------------------------')

# CHARACTERS
''' c presentation type formats an integer character code as the 
corresponding character'''
print(f'{65:c} {97:c}')         # Using char type to make an 'A' & 'a'
print('--------------------------------')

# STRINGS
'''S PRESENTATION TYPE is the default. If you specify "s" 
explicitly the value to format must be a var that ref a string,
an expression that produces a string or string lit'''

'''If you do not specify a presentation type, as in the second 
placeholder below, non-string values like the integer 7 are converted
to strings:'''
print(f'{"hello":s} {7}')

# FLOATING-POINT AND DECIMAL VALUES
'''Exponential (scientific) notation can be used to format the values 
more compactly'''
print(f'{Decimal("10000000000000000000000000000000000.0"):.3f}')    # Floating-point numbers
print(f'{Decimal("10000000000000000000000000000000000.0"):.3e}')    # Exponential Numbers
print(f'{Decimal("10000000000000000000000000000000000.0"):.3E}')    # Can use capital or lowercase
print('-------------------------------------------------')
# FIELD WIDTHS AND ALIGNMENT
'''Right-aligns numbers & left-aligns strings'''
print(f'[{27:10d}]')
print(f'[{3.5:10f}]')
print(f'[{"hello":10}]')
print('---------------------------')

# EXPLICITLY SPECIFYING LEFT AND RIGHT ALIGNMENT IN A FIELD
'''Can specify left and right alignment w/ < and >'''
print(f'[{27:<15d}]')
print(f'[{3.5:<15f}]')
print(f'[{"hello":>15}]')
print('------------------------------')

# CENTERING A VALUE IN A FIELD
print(f'[{27:^7d}]')
print(f'[{3.5:^7.1f}]')
print(f'[{"hello":^7}]')
print('----------------------------------')


# NUMERIC FORMATTING
'''Formatting Positive Numbers with Signs'''
print(f'[{27:+10d}]')
''' To fill the remaining characters of the field with 0s rather than
spaces, place a 0 before the field width (and after the + if there
is one)'''
print(f'[{27:+010d}]')

# Using a Space Where a + Sign Would Appear in a Positive Value
print(f'{27:d}\n{27: d}\n{-27: d}')     #Space after ':' can align output
print('-----------------------------')
# Grouping Digits
print(f'{12345678:,d}')         #Thousands seperator by the ','
print(f'{123456.89:,.2f}')
print('---------------------------------')

# STRINGS format METHOD
print('{:.2f}'.format(17.489))      # OLD format style
print('---------------------------')
# Multiple PlaceHolders
'''Old FORMAT method with multiple placeholders'''
print('{} {}'.format('Amanda', 'Cyan'))
print('---------------------------')

# Referencing Arguments By Position Numbers
'''The format string can reference specific arguments by their 
position in the format method’s argument list, starting with 
position 0'''

print('{0} {0} {1}'.format('Happy', 'Birthday'))
'''[ABOVE] Can use the same position number (i.e. {0} above) as
many times as you want to '''

# Referencing Keyword Args
'''You can reference keyword args by their keys in the placeholder'''
print('{first} {last}'.format(first='Amanda', last='Gray'))
print('{last} {first}'.format(first='Amanda', last='Gray'))


