for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("frizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)