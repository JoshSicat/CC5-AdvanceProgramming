#function to calculate the value in the list 
def calculate_product(input_list):
    product = 1 
    for value in input_list:
        product *= value
    return product

# the example of the list 
my_list = [2, 15, 20, 8, 6]

#calculate the product of the value  in the list using the function
result = calculate_product(my_list)

# display of the result 
print(f"the product of the values in the list is: {result}")