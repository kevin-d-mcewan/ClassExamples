import csv

# WRITING TO A CSV FILE
with open('accounts.csv', mode = 'w', newline = '') as accounts:
	''' [writer] F(x) returns an object that writes CSV data to 
	specified file object. Each call to [writerow] method receives
	an iterable to store in the file'''
	writer = csv.writer(accounts)
	writer.writerow([100, 'Jones', 24.98])
	writer.writerow([200, 'Doe', 345.67])
	writer.writerow([300, 'White', 0.00])
	writer.writerow([400, 'Stone', -42.16])
	writer.writerow([500, 'Rich', 224.62])

# READING FROM A CSV FILE
with open('accounts.csv', 'r', newline = '') as accounts:
	print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
	reader = csv.reader(accounts)
	for record in reader:
		account, name, balance = record
		print(f'{account:<10}{name:<10}{balance:>10}')



