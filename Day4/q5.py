import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_set = pd.read_csv("C:\\Users\\KIIT\\Downloads\\Social_Network_Ads.csv")


sns.lmplot(x='Age', y='EstimatedSalary', data=data_set, fit_reg=False, hue='Purchased', legend=True, palette="Set1")
plt.show()