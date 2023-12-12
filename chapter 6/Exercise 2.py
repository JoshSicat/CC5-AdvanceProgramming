a = [20, 23, 15, 8, 54, 36, 15, 10]

#finding the indices of even numbers
even_indices = [index for index, value in enumerate(a) if value % 2 == 0]
print("Indices of even numbers: ", even_indices)

#sorting the array
sorted_array = sorted(a)
print("sorted array:", sorted_array)

#slicing thr elements from index 3 to  the end of array
slice_3_to_end = a[3:]
print("slice from index 3 until the end: ", slice_3_to_end)

#slicing again the  elements from index 0 to 4
slice_0_to_4 = a[5:]
print("slice from index 0 to 4: ", slice_0_to_4)

#printing the number using the negative slcicing
negative_slice = a[-5:-2]
print("using negative slicing to get get [54, 10, 36]: ", negative_slice)