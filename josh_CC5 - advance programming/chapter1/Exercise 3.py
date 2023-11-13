#geting the lengths of the sides from the user
side1 = float(input("enter the length of side 1: "))
side2 = float(input("enter the length of side 2: "))
side3 = float(input("enter the length of side 3: "))

#triangle inequality
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("these side lengths can form a triangle.")

else:
    print("these side lengths cannot form a triangle.")