import pandas as pd
import seaborn as sns

data_set = pd.read_csv("C:\\Users\\KIIT\\Downloads\\Social_Network_Ads.csv")

sns.displot(data_set['EstimatedSalary'])
