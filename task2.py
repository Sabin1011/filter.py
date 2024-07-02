import pandas as pd

dataframe = pd.read_csv('student.csv')
print("our dataframe...",dataframe)
dataframe_subset = dataframe[['first_name','last_name']]
dataframe_filtered = len(dataframe['first_name']) >5
print(dataframe.isnull().sum())
dataframe.dropna(inplace=True)
dataframe.drop_duplicates(inplace=True)


