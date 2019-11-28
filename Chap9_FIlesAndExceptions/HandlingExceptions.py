# dividebyzero.py
"""SImple exception handling example."""

while True:
	# attempt to convert and divide values
	try:
		number1 = int(input('Enter numerator: '))
		number2 = int(input('Enter denominator: '))
		result = number1 / number2
	except ValueError:    # Tried to convert non-numeric value to int
		print('You must enter two integers\n')
	except ZeroDivisionError:   # Denominator was 0
		print('Attempted to divide by 0\n')
	else:   # Executes only if no exceptions occur
		print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
		break   # Terminate the loop






