''' Use a WITH statement to update the ACCOUNTS.TXT file to change
account 300's name from "White" to "Williams" '''

# OPENING both txt files
accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')

''' Using WITH statement to use both files and then for every
record in the file SPLIT by 3 columns. If it is not record 300
write the record directly to TEMP_FILE "ELSE" create a new record
to rewrite "Williams" in place of "White". Then write to file'''
with accounts, temp_file:
	for record in accounts:
		account, name, balance = record.split()
		if account != '300':
			temp_file.write(record)
		else:
			new_record = ' '.join([account, 'Williams', balance])
			temp_file.write(new_record + '\n')

''' Import OS (which should be done at top of file '''
import os

'''Now we are removing old account file with wrong entry & then
renaming "temp_file" to "accounts.txt" file like the one deleted'''
os.remove('accounts.txt')
os.rename('temp_file.txt', 'accounts.txt')






