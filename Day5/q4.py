section_girls = ["A","B","C"]
section_boys = ["A", "B", "C", "D", "E"]

list_girls_section = []
lis_boys_section = []

for i in section_girls:
    list_girls_section.append(int(input(f"Enter Number of girls in Section {i}")))

print("\n\n")

for i in section_boys:
    lis_boys_section.append(int(input(f"Enter Number of Boys in Section {i}")))

print("\n\n")

print(f"Total number of Boys is : {sum(lis_boys_section)}")
print(f"Total number of girls is : {sum(list_girls_section)}")
print(f"Total number of students is : {sum(list_girls_section)+sum(lis_boys_section)}")
