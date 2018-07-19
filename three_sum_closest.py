## Problem: Given an array nums of n integers and an integer target, 
## find three integers in nums such that the sum is closest to target. 
## Return the sum of the three integers. 
## You may assume that each input would have exactly one solution.

import sys
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



## Algorithm fails when there is negative targets

def three_sum_closest(arr,n,target):

	lst = []
	quicksort(arr,0,n)
	print arr
	min_diff = sys.maxint

	for i in range(n-1):
		l = i + 1
		r = n

		while l<r:

			add = arr[i] + arr[l] + arr[r]
			diff = target-add

			if add > target:
				r = r - 1

			if add < target:
				l = l + 1

			if add == target:
				raise ValueError('Sum of three entries match the target')

			if min_diff > diff:
				min_diff = diff

	return (target-min_diff)


arr = [-1,2,1,-4]
# arr = [1,2,4,3,9,7,5]
n = len(arr)-1
target = 1

lst = three_sum_closest(arr,n,target)
# print lst
print "The sum that is closest to the target %d is: %d" %(target,lst)











