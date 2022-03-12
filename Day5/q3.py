age = int(input("Enter your age: "))


def age_remain(val):
    if 65 - val > 0:
        return f"You will retire in {65 - val} years"
    elif 65 - val == 0:
        return "You Retired this year"
    else:
        return "You Already Retired"


print(age_remain(age))
