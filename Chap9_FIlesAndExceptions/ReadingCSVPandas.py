'''Working with Locally Stored CSV Files'''

import pandas as pd

df = pd.read_csv('accounts.csv',
                 names = ['account', 'name', 'balance'])

print(df)

'''Save a [DataFrame] to a file using CSV format, call [DataFrame]
method [to_csv] '''

df.to_csv('accounts_from_dataframe.csv', index = False)
