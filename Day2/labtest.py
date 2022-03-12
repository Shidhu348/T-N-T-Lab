import pandas as pd

df = pd.read_csv("C:\\Users\\KIIT\\Downloads\\Data.csv")

print(df)
print("\n")

sal_class = []

for i in range(len(df)):

    sal = df['Salary'][i]

    if sal > 70000:
        sal_class.append('class0')
    elif sal >= 61000:
        sal_class.append('class1')
    elif sal >= 48000:
        sal_class.append('class2')
    else:
        sal_class.append('')

df['Salary_class'] = sal_class

print(df)
print("\n")

sal_class = []

i = 0
while i < 10:

    sal = df['Salary'][i]

    if sal > 70000:
        sal_class.append('class0')
    elif sal >= 61000:
        sal_class.append('class1')
    elif sal >= 48000:
        sal_class.append('class2')
    else:
        sal_class.append('')

    i += 1

print(df)
print("\n")

print(df["Salary_class"].value_counts())
print("\n")


age_con = df['Age'] * 12

df['Age_Converted'] = age_con


print(df)
print("\n")
