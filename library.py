days = int(input("Enter days:"))
if days<5:
    charges = 2*days
    print("enter charge for library",charges)
elif days>=6 and days<=10:
    charges = 3*days
    print("enter charge for library",charges)
elif days>=11 and days<=15:
    charges = 4*days
    print("enter charge for library",charges)
elif days>15:
    charges = 5*days
    print("enter charge for library",charges)
else:
    print("your total charges")
