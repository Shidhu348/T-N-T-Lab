amt = int(input("Enter total amount : "))
print("Jean pants the person can afford : ", amt // 750)
print("Money needed to afford an additional jean pant : ", (750 - (amt - 750 * (amt // 750))))
