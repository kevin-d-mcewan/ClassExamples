# Running Try with Finally

try:
	print('try suite with no exception raised')
except:
	print('this will not execute')
else:
	print('else executes because no exception in the try suite')
finally:
	print('finally always executes')

print('-------------------------------------------------')
'''TRY statement in which an exception occurs'''
# ValueError after first print stmnt to prove finally always runs
try:
	print('try suite that raises an exception')
	int('hello')
	print('this will not execute')


except ValueError:
	print('a ValueError occurred')

else:
	print('else will not execute bc an exception occurred')

# Finally will always run even with an error
finally:
	print('finally always executes')

print('------------------------------------------------')
'''Combinging WITH stmnt and TRY EXCEPT stmnt'''

try:
	with open('gradez.txt', 'r') as accounts:
		print(f'{"ID":<3}{"Name":<7}{"Grade"}')
		for record in accounts:
			student_id, name, grade = record.split()
			print(f'{student_id:<3}{name:<7}{grade}')
except FileNotFoundError:
	print('The file name you specified does not exist')
