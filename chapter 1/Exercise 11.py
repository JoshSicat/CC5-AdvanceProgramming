#given tumple
year = (2017, 2003, 2020, 2004, 2000, 2023, 8006, 1420, 2021)

#accessing  the value of  index -3
value_at_index_minus_3 = year[-3]
print("Value at index -3:", value_at_index_minus_3)

#reverse the tumple 
reversed_year = tuple(reversed(year))
print("Original tumple:", year)
print("Reversed timple:", reversed_year)

#the number of times 2004
count_2004 = year.count(2004)
print("number of times 2004  is in  tumple:", count_2004)

#the index 8006
index_of_8006 = year.index(8006)
print("index value of 8006:", index_of_8006)

#length of the given tuple
length_of_tuple = len(year)
print("length of the  tumple:", length_of_tuple)