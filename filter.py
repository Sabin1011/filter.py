import pandas as pd
data = {'Name':['Alice', 'Bob', 'Charlie', 'David'],
        'Age':[20,30,35,40],
        'City':['Newyork', 'Losangeles', 'Chicago', 'Houston']}
df=pd.DataFrame(data)
filtered_df = df[df['Age']>30]
print(filtered_df)