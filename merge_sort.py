def merge(arr,l,mid,r):

	n1 = mid-l+1
	n2 = r - mid

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0,n1):
		L[i] = arr[i+l]
	for j in range(0,n2):
		R[j] = arr[mid+j+1]

	# Merge the temp arrays back into a complete sorted array
	i = 0	# initial index of first subarray
	j = 0	# initial index of second subarray
	k = l   # initial index of merged subarray

	while i < n1 and j < n2:
		if L[i]<=R[j]:
			arr[k] = L[i]
			i = i+1
		else:
			arr[k] = R[j]
			j = j+1
		k = k+1

	while i < n1:
		arr[k] = L[i]
		i = i+1
		k = k+1

	while j < n2:
		arr[k] = R[j]
		j = j+1
		k = k+1


def merge_sort(arr,l,r):
	if r>l:

		mid = (l+(r))/2
		merge_sort(arr,l,mid)
		merge_sort(arr,mid+1,r)
		merge(arr,l,mid,r)


# Driver code
print("Please enter some numbers: ")
str_arr = raw_input().split(' ')
arr = [int(num) for num in str_arr]

r = len(arr)
merge_sort(arr,0,r-1)
print("Sorted array is: ")
for k in range(len(arr)):
	print("%d" %arr[k])

