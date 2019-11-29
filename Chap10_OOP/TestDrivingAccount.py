from account import Account
import os

from decimal import Decimal

value = Decimal('12.34')

''' Use a constructor expression to create an Account object and 
initialize it with an account holders name (a string) and balance
(a Decimal)'''

account1 = Account('John Green', Decimal('50.00'))

# Getting an Account's Name and Balance
print(account1.name)
print(account1.balance)

# Use Account's deposit method to input + $ and add to balance
account1.deposit(Decimal('25.53'))
print(account1.balance)



