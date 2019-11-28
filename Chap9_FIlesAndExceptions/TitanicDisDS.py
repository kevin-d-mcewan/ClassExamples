import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
                      'Rdatasets/csv/carData/TitanicSurvival.csv')

pd.set_option('precision', 2)   # Format fo floating-point values
# print(titanic.head())   # Prints 1st 5 data points
# print('----------------------------------------------')
# print(titanic.tail())   # Prints last 5 data points
# print('----------------------------------------------')
# print(titanic)      # Prints 1st and last 5 data points
# print('----------------------------------------------')
# print('----------------------------------------------')
titanic.columns = ['names', 'survived', 'sex', 'age', 'class']
print(titanic.head())
print('------------------------------------')
print(titanic.describe())   # CALC statistics of dataset
print('------------------------------------')
print(titanic.describe().head())
print('------------------------------------')

'''Stats about people who survived. By using one of the two answers
we are able to group all of them and get the stats from that group'''
print((titanic.survived == 'yes').describe())
print('------------------------------------')

# 9.12.5 Passenger Age Histogram
import matplotlib

histogram = titanic.hist()
histogram.display()