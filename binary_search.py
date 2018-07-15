### Problem: Given a sorted array arr[] of n elements
### write a function to search a given element x in arr[].


## Time complexity: O(logn)
## Input array must be sorted in ascending order

def binary_search(arr,low,high,x):

	if high>=low:

		mid = low + (high-low)/2

		if arr[mid] == x:
			return mid

		elif arr[mid] > x:
			return binary_search(arr,low,mid-1,x)
		else:
			return binary_search(arr,mid+1,high,x)


arr = [2, 3, 4, 10, 40, 44, 68, 77, 89, 98]
x = 89
n = len(arr)-1
k = binary_search(arr,0,n,x)  # 8
print "The required element is at index:", k

