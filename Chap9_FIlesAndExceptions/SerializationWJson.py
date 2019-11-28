import json

# SERIALIZING AN OBJECT TO JSON
accounts_dict = {'accounts': [
	{'account': 100, 'name': 'Jones', 'balance': 24.98},
	{'account': 200, 'name': 'Doe', 'balance': 345.67}]}

with open('accounts.json', 'w') as accounts:
	json.dump(accounts_dict, accounts)


# DESERIALIZING THE JSON TEXT
with open('accounts.json', 'r') as accounts:
	accounts_json = json.load(accounts)

# INTERACT w/ loaded OBJ, display the DICT:
print(accounts_json)
print('--------------------------')
# ACCESS dict contents. Get list of dictionary associated w 'accounts'
print(accounts_json['accounts'])
print('------------------------------')
# Getting individual account dictionaries
print(accounts_json['accounts'][0])
print('------------------------------')
print(accounts_json['accounts'][1])
print('-------------------------------')


# DISPLAYING THE JSON TEXT
with open('accounts.json', 'r') as accounts:
	print(json.dumps(json.load(accounts), indent = 4))



