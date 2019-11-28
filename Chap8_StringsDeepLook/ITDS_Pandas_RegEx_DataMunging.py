import pandas as pd

zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
print(zips)
print('---------------------------')

print(zips.str.match(r'\d{5}'))
print('--------------------------------')


cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
print(cities)
print('-----------------------------------------')
'''The RegEx is looking for a space and then followed by 2 
UPPERCASE letters'''
print(cities.str.contains(r' [A-Z]{2}'))
print('----------------------------------------')

print(cities.str.match(r' [A-Z]{2} '))
print('-----------------------------------------')

# REFORMATTING YOUR DATA
contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
            ['Sue Brown', 'demo2@deitel.com', '5555551234']]
contactsdf = pd.DataFrame(contacts,
                          columns = ['Names', 'Email', 'Phone'])

print(contactsdf)
print('--------------------------------------------------')

import re

def get_formatted_phone(value):
	result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
	return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Phone'].map(get_formatted_phone)
print(formatted_phone)
print('--------------------------------------------------')

contactsdf['Phone'] = formatted_phone
print(contactsdf)





