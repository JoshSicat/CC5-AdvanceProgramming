#taking 2 integer inputs from the user
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number:"))

#calculations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
remainder_result = num1 % num2

#the results
print(f"sum: {num1} + {num2} = {sum_result}")
print(f"difference: {num1} - {num2} = {diff_result}")
print(f"product: {num1} * {num2} = {product_result}")
print(f"quotient: {num1} / {num2} = {quotient_result}")
print(f"remainder: {num1} % {num2} = {remainder_result}")