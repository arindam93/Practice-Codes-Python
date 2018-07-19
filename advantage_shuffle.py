## Problem: Given two arrays A and B of equal size, 
## the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
## Return any permutation of A that maximizes its advantage with respect to B.

## Time complexity: O(nlogn)
## Space complexity: O(n)

from heapq import heapify, heappop

def advantage_shuffle(arr1,arr2):

	n = len(arr1)
	m = len(arr2)

	if n != m:
		raise ValueError("The arrays must be of same size")

	lst = [0] * n
	heapify(arr1)   ## create a min heap

	sorted_b = [(b,i) for i,b in enumerate(arr2)]
	sorted_b.sort()   ## list of tuples containing (value, index) sorted acc to value

	unused = []

	for b, i in sorted_b:
		while arr1:
			a = heappop(arr1)
			if a > b:
				lst[i] = a
				break

			else:
				unused.append(a)


	## now put the unused values in appropriate indices 
	k = len(unused)

	for j in range(n-k,n):
		lst[sorted_b[j][1]] = unused[j-(n-k)]

	return lst, unused

# arr1 = [2,7,11,15]
# arr2 = [1,10,4,11]

arr1 = [10, 2, 15, 8]
arr2 = [3, 11, 4, 10]
lst, unused = advantage_shuffle(arr1,arr2)

print "The advantage array is:", lst


