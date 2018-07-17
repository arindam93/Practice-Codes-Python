## Problem: Find the kth largest element in an unsorted array. 
## Note that it is the kth largest element in the sorted order, 
## not the kth distinct element.

## Simplest approach: sort the array and access the element by its index

## Time complexity: O(nlogn)  ## sorting using heapsort
## Space complexity: O(1)

def find_largest(arr,k):

	arr = sorted(arr)

	output = arr[-k]
	return arr, output



arr = [3,2,1,5,6,4,9,12,8,11,20]
k = 3
arr, tmp = find_largest(arr,k)
print arr
print ("The %dth largest element is: %d"  %(k,tmp))