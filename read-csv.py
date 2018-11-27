import pandas as pd
data = pd.read_csv('/home/ubuntu/DataScience/input.csv')
print(data)

#Get the results of the salary column
print(data[0:7]['salary'])

#Print values of name and salary columns
print(data.loc[:, ['name', 'salary']])

#Dispaly name, salary and dept
print(data.loc[:, ['name', 'salary', 'dept']])

#Display information for IT employees
print(data.loc[[0,2,5],['name','salary','dept']])
