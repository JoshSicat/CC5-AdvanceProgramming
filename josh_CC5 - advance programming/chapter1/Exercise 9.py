# creating a int list with 10 values
int_list = [23, 5, 19, 8, 31, 12, 4, 9, 20, 16]

#the output of list using a for loop
print("list using a for loop:")
for num in int_list:
    print(num, end=" ")
print()

#the highest and the lowest value
print(f"highest value: {max(int_list)}")
print(f"lowest value: {max(int_list)}")

# sort the number by order
int_list.sort()
print("sorted list in descending order:", int_list)

# reversing the number 
int_list.sort(reverse=True)
print("sorted list in descending order:", int_list)

#adding two elements
int_list.append(27)
int_list.append(2)

print("list after appending:", int_list)