import pandas as pd


data_set = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv").dropna()
# q1
data_set1 = data_set.copy(deep=True)
print(data_set)
# q2
print(data_set['Country'].value_counts())
# q3
print(pd.crosstab(index = data_set['Country'], columns = data_set['Purchased'], dropna = True))







