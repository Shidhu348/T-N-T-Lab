import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_set = pd.read_csv("C:\\Users\\KIIT\\Downloads\\Social_Network_Ads.csv")
sns.set(style="darkgrid")
sns.regplot(x=data_set['Age'], y=data_set['EstimatedSalary'], marker="*", fit_reg=False)
plt.show()