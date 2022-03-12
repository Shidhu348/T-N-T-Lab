import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_set = pd.read_csv("D:\\6thSemLab\\TnTLab\\Day3\\Data.csv")


sns.boxplot(x=data_set['Age'], y=data_set['Country'])
plt.show()