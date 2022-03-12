import matplotlib.pyplot as plt
import pandas as pd

social_network_data = pd.read_csv("C:\\Users\\KIIT\\Downloads\\Social_Network_Ads.csv")
plt.hist(social_network_data['EstimatedSalary'], color='blue', edgecolor = 'white', bins=4)
plt.title("Q1 Graph")
plt.xlabel("Estimated Salary")
plt.ylabel("Count")
plt.show()
