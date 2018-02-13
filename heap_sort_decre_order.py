
def max_heapify(arr,i,n):
	l = 2*i
	r = 2*i + 1

	if (l<=n and arr[l]>arr[i]):
		largest = l
	else:
		largest = i

	if (r<=n and arr[r]>arr[largest]):
		largest = r

	if largest != i:
		tmp = arr[i]
		arr[i] = arr[largest]
		arr[largest] = tmp
		max_heapify(arr,largest,n)

def heap_sort(arr,n):
	k = 0
	new_arr = [0] * (n+1)
	while n>=0:
		for i in range(n/2,-1,-1):
			max_heapify(arr,i,n)
		swap = arr[0]
		arr[0] = arr[n]
		arr[n] = swap

		new_arr[k] = arr[n]
		k = k+1
		n = n-1

	return new_arr

# Driver code
print("Please enter some numbers: ")
str_arr = raw_input().split(' ')
arr = [int(num) for num in str_arr]

# arr = [16, 4, 10, 14, 1, 9, 12, 17, 11, 7]
n = len(arr)-1
new_arr = heap_sort(arr,n)
print("Sorted array is: ")
for k in range(len(new_arr)):
	print("%d" %new_arr[k])




