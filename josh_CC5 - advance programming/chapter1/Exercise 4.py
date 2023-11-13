#inputing the three number
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
num3 = float(input("enter the third number: "))

#checking the largest number using id-else statements
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largets = num2
else:
    largest = num3

print(f"the largest number is: {largest}")