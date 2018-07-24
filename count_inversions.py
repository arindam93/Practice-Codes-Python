# -*- coding: utf-8 -*-


## Program to check inversions in an array

## Inversion Count for an array indicates: how far (or close) the array is from being sorted
## If array is already sorted then inversion count is 0. 
## If array is sorted in reverse order that inversion count is the maximum. 
## Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

## Method 1: Simple
## For each element in the array, count the number of elements on its right which are smaller.
## Time Complexity: O(N*N)
## Space Complexity: O(1)

def inversions(arr):
	n = len(arr)-1

	count = 0
	for i in range(0,n):
		for j in range(i+1,n+1):
			if arr[i] > arr[j]:
				count = count + 1

	return count


## Test code
arr = [1, 20, 6, 4, 5]
k = inversions(arr)
print "The number of inversions in the array:", k



## Method 2: Using Merge Sort




