def peak1D(arr):
	'''This function recursively finds a peak in a 1D array. Complexity: O(logn)'''

	if not arr:
		return -1

	start = 0
	stop = len(arr) - 1

	while True:
		mid = (stop+start)//2

		if arr[mid] < arr[mid-1]:
			stop = mid

		elif arr[mid+1] > arr[mid]:
			start = mid

		else:
			return mid

	# mid = start if arr[start] > arr[stop] else stop
	# return mid

arr = [2, 7, 6, 4, 5, 8, 1, 5, 3, 7, 11, 2, 3]
p = peak1D(arr)
print arr[p]






