from account import Account


from decimal import Decimal

value = Decimal('12.34')

''' Use a constructor expression to create an Account object and 
initialize it with an account holders name (a string) and balance
(a Decimal)'''

account1 = Account('John Green', Decimal('50.00'))

# Getting an Account's Name and Balance
print(account1.name)
print(account1.balance)


