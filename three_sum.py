### Problem: Given an array and a number x, check for triplets the array with sum as x

def partition(arr,low,high):
	i = (low)-1
	pivot = arr[high]

	for j in range(low,high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1


def quicksort(arr,low,high):

	if low<high:

		pi = partition(arr,low,high)
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)


def three_sum(arr,n,x):

	lst = []
	quicksort(arr,0,n)

	for i in range(n-1):
		l = i+1
		r = n

		while l<r:

			sum = arr[i] + arr[l] + arr[r]
			if (sum == x):
				lst.append([arr[i],arr[l],arr[r]])
				l = l+1
				r = r-1

			elif sum < x:
				l = l+1
			elif sum > x:
				r = r-1

	return lst

## Driver Code to test the algorithm

arr = [3,2,4,1,5,7,8,6]
n = len(arr)-1
lst = three_sum(arr,n,8)  # find triplets in the array that sum to 8
print lst


