from decimal import Decimal

'''Account class definition'''


class Account:
	"""Account class for maintaining a bank account balance"""

	def __init__(self, name, balance):
		"""Initialize an Account Object"""

		# If balance is less that 0.00, raise an Exception
		if balance < Decimal('0.00'):
			raise ValueError('Initial balance must be >= 0.00')

		self.name = name
		self.balance = balance

	def deposit(self, amount):
		"""Deposit money to the account"""

		# If amount is less that 0.00, raise an exception
		if amount < Decimal ('0.00'):
			raise ValueError ('Amount must be positive')

		self.balance += amount
