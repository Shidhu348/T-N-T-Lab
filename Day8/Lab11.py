import numpy as np

# Q1. Create Lists ,Tuples, Dictionaries and Sets.Print elements stored in each case.
q1list = [1,2,3,4,5,6,7]
print(q1list)

thisdict = {
  "name": "xyz",
  "roll": "1905348",
  "year_of_passing": 2023
}
print(thisdict)

myset = {1,2,3,4,4,5,7}
print(myset)

print("\n")

# Q2.I) Select the Element kept at 2 nd position. From a List and display it.
# Ii)create numpy array by already existing list and display its datatype and dimension.

# Ans.I)
q1list = [1,2,3,4,5,6,7]
nplist = np.array(q1list)
print(nplist[1])

# Ans. II)
print(nplist.dtype)
print(np.shape)

print("\n")

# Q3.	Use range function to generate values with name RangeVar. Keep lower bound as 1, higher bound 50. and each value should have difference of 10
RangeVar = range(1, 50, 10)
for i in RangeVar:
    print(f"{i} ")

print("\n")

# Q4.	Create a string ‘Techniquelab’. Find out the character at 5th position. Find out the index of ‘l’ in the string.
a = "Techniquelab"
print(a[5])
index = a.index('i')

print('The index of i:', index)

print("\n")

# Q5.	In 3rd question, the values populted in RangeVar.Find out if 11 exists and also find out the value at 3rd index.
a = list(range(1, 50, 10))
print(11 in a)
print(f'at 3rd index = {a[3]}')

print("\n")

# Q6.	Create a list with values 100, ‘Alice’, 12 and ‘Programmer’.Display the whole list.Then add value ‘Python’ to the list and display the modified list.
q6list = [100, 'Alice', 12, 'Programmer']
print(q6list)
q6list.append('Python')
print(q6list)

print("\n")

# Q7.	Create a tuple with values:100, ‘Alice’, 12 and ‘Programmer’.Display the tuple.Then add values ‘Python’ and
# ‘ML’ to it and display the modified tuple.
q7list = (100, 'Alice', 12, 'Programmer')
print(q7list)
q7list+= ('Python', 'ML')
print(q7list)

print("\n")

# Q8. In the tuple with values :100, ‘Alice’, 12 and ‘Programmer’,print the values from index 0 to 2 ,
# getting displayed on console thrice.
q8list = tuple([100, 'Alice', 12, 'Programmer'])
for i in range(0, 3):
    print(q8list[0:3])

print("\n")
 





