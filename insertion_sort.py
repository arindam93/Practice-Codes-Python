def insertion_sort(arr):

	for i in range(len(arr)-1):
		key = arr[i+1]
		while i>=0 and arr[i]>key:
			tmp = arr[i]
			arr[i] = key
			arr[i+1] = tmp
			i = i-1

# Driver code
print("Please enter some numbers: ")
str_arr = raw_input().split(' ')
arr = [int(num) for num in str_arr]
# arr = [7, 5, 4, 3, 6, 1, 5, 9, 2, 10, 3, 1, 0, 6, 7, 4, 2, 8, 9, 7, 4]
insertion_sort(arr)
print("Sorted array is: ")
for k in range(len(arr)):
	print("%d" %arr[k])