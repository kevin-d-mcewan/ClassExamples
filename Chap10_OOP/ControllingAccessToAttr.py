from account import Account
from decimal import Decimal

'''Initialize and creates acct1 '''
account1 = Account('John Green', Decimal('50.00'))
print(account1.balance)

# Set balance to neg value then display
account1.balance = Decimal('-1000.00')
print(account1.balance)
"""Unlike methods, data attr. cant validate values assigned to them"""

# ENCAPSULATION
""" CLIENT CODE is any code that uses objects of the class.
Most OOP languages enable you to ENCAPSULATE (or 'hide') an obj's
data from CLIENT CODE. This data is said to be PRIVATE DATA """

# PRIVATE AND PUBLIC ATTRIBUTES
""" Python has no PRIVATE DATA. If something is said to be private
convention says to lead with double underscores. This is for 
INTERNAL CLASS USE ONLY.

Public Accessible data does not have the leading double underscores.

However, with that said it is only by naming convention. Just bc
you shouldn't use those doesn't mean you can't but follow the
advise of the programmer."""













