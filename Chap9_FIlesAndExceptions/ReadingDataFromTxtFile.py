'''The following session reads records from the file accounts.txt and
displays the contents of each record in columns with the Account and
Name columns left aligned and the Balance column right aligned, so
the decimal points align vertically'''

with open('accounts.txt', mode = 'r') as accounts:
	print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
	for record in accounts:
		account, name, balance = record.split()
		print(f'{account:<10}{name:<10}{balance:>10}')





