print("Enter Marks Obtained in 4 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())

total = markOne+5+markTwo+5+markThree+markFour+5
avg = total/4

if 91 <= avg <= 100:
    print("Your Grade is A1")
elif 81 <= avg < 91:
    print("Your Grade is A2")
elif 71 <= avg < 81:
    print("Your Grade is B1")
elif 61 <= avg < 71:
    print("Your Grade is B2")
elif 51 <= avg < 61:
    print("Your Grade is C1")
elif 41 <= avg < 51:
    print("Your Grade is C2")
elif 33 <= avg < 41:
    print("Your Grade is D")
elif 21 <= avg < 33:
    print("Your Grade is E1")
elif 0 <= avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")
    
