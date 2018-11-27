#Example 1
#More than one dimension
import numpy as np
import pandas as pd

a = np.array([[1,2], [3,4]])
print (a)

#example 2
#minimum dimensions
x = np.array([1,2,3,4,5], ndmin = 2)
print (x)

#Example 3
#dtype parameter
y = np.array([1,2,3], dtype = complex)
print(y)

#create a series from a Numpy Array
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data)
print(s)

#Pandas DataFrame
dataFrame = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28,34,39,45]}
dF = pd.DataFrame(dataFrame, index=['rank1', 'rank2', 'rank3', 'rank4'])
print(dF)
