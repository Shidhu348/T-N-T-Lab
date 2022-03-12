import pandas as pd

data_set = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv").dropna()
# q1
data_set1 = data_set.copy(deep=True)
print(data_set)
# q2
print(data_set['Country'].value_counts())
# q3
data_set = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv").dropna()
print(pd.crosstab(index = data_set['Country'], columns = data_set['Purchased'], dropna = True))
# q4
print(data_set)
print(pd.crosstab(index= data_set['Country'], columns=data_set['Purchased'], normalize=True, dropna = True))
print(pd.crosstab(index= data_set['Country'], columns=data_set['Purchased'],normalize=True, margins=True, dropna=True))
print(pd.crosstab(index= data_set['Country'], columns=data_set['Purchased'],normalize='columns', margins=True, dropna=True))
print(pd.crosstab(index= data_set['Purchased'], columns=data_set['Country'],normalize='columns', margins=True, dropna=True))
# q5
print(data_set)
print(data_set.corr(method='pearson'))








