count = 0 #initianlizing the count of loop

while True:
    user_input = input("would you like th continue? (enter Y for yes, any other key to exit): ")
    if user_input.upper() == 'Y':
        count += 1
    else:
        break

print(f"the loop executed {count} times.")