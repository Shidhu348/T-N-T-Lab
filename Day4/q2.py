import matplotlib.pyplot as plt

counts = [3,3,3]
country = ('France','Germany','Spain')
plt.bar(country,counts,color = ['red','blue','green'])
plt.title('Country count')
plt.xlabel('country')
plt.ylabel('counts')
plt.show()