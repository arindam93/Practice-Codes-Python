## Problem: There are 2 sorted arrays A and B of size n each. 
## Write an algorithm to find the median of the array obtained 
## after merging the above 2 arrays(i.e. array of length 2n). 


# Method 1 (merge routine of merge sort)
# Time complexity: O(n)

def median_two_sorted_arrays(arr1,arr2):

	n = len(arr1)
	m = len(arr2)
	lst = [] ## merged array
	i = 0
	j = 0

	while i<n and j<m:
		if (arr1[i] < arr2[j]):
			lst.append(arr1[i])
			i = i+1
		else:
			lst.append(arr2[j])
			j = j+1


	# code snippet to return median if the arrays are of same size 
	# (the merged size will be even always)

	# if (i == n and j == 0):
	# 	m2 = arr2[0]
	# 	return lst, (lst[-1]+m2)/2.0

	# if (i == 0 and j == m):
	# 	m1 = arr1[0]
	# 	return lst, (lst[-1]+m1)/2.0

	# if (i == n or j == m):
	# 	return lst, (lst[-1]+lst[-2])/2.0

	# code snippet to return median if the arrays are of different size

	if i<n:
		while i<n:
			lst.append(arr1[i])
			i = i+1
	if j<m:
		while j<m:
			lst.append(arr2[j])
			j = j+1

	k = len(lst)
	if (k%2) != 0:
		return lst, lst[(k-1)/2]
	else:
		return lst, (lst[k/2]+lst[(k-1)/2])/2.0


#arr1 = [10,15,20,25,30,35,37,40]
# arr1 = [1,3,5,7,9,11,13,15,23]
# arr2 = [20,60,80,90,98,102,110,120]
arr1 = [1,3,5,7,9,11,13,17,40,100]
arr2 = [6,8,10,12,14,16,18,20,60,90]

lst, _median = median_two_sorted_arrays(arr1,arr2)
print "The first array is:", arr1
print "The second array is:", arr2
print "The merged array is:", lst
print "The median of merged array is:", _median