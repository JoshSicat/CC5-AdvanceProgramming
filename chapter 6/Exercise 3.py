import operator  

#display the culatulaing menu
menu = """""
Caculate Menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Modulus
6. Check greater number
"""
print(menu)

#dictionary to map user choice operator
operations = {
    1: operator.add,
    2: operator.sub,
    3: operator.mul,
    4: operator.truediv,
    5: operator.mod,
    6: max
}

#asking the user to choose operator
operation_choice = int(input(" choose a number (1-6): "))

#asking the user to input a values
num1 = float(input("Type first number: "))
num2 = float(input("Type second number:"))

#perform calculation and the result
if operation_choice in operations:
    result = operations[operation_choice](num1, num2)
    print("Result: ", result)
else:
    print("Invalid choice. please choose a number between (1-6).")