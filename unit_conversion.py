weight = int(input("Please enter the weight of the unit: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"The weight is {converted} lbs.")
else:
    converted = weight * 0.45
    print(f"The weight is {converted} kilos.")