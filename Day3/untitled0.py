
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("S_A_V.csv")

print(df)

plt.scatter(
        df['Age'],
        df['EstimatedSalary']
        )
plt.title('Graph Ques 6')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')

plt.show()
