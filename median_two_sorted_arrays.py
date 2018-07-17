### Problem: There are 2 sorted arrays A and B of size n each. 
### Write an algorithm to find the median of the array obtained 
### after merging the above 2 arrays(i.e. array of length 2n). 

###The complexity should be O(log(n)).


## Time complexity: O(logn) (Divide and conquer paradigm)


## function to return the median of two arrays
def find_median(arr1,arr2,m,n):


	if (m%2) == 0:
		m1 = (arr1[m/2] + arr1[(m-1)/2])/2.0
	else:
		m1 = float(arr1[m/2])

	if (n%2) == 0:
		m2 = (arr2[n/2] + arr2[(n-1)/2])/2.0
	else:
		m2 = float(arr2[n/2])

	return m1, m2


def median_binary_search(arr1,arr2):

	len1 = len(arr1)
	len2 = len(arr2)

	print arr1
	print arr2

	m1, m2 = find_median(arr1,arr2,len1,len2)

	mid1 = len1/2
	mid2 = len2/2

	if (len1 == 2 and len2 == 2):
		return (max(arr1[0],arr2[0]) + min(arr1[1],arr2[1]))/2.0  # final median

	elif (m2 > m1 and len1 > 2 and len2 > 2):

		if (len2%2) != 0:
			mid2 = mid2 + 1

		arr1 = arr1[mid1:]
		arr2 = arr2[:mid2]
		return median_binary_search(arr1,arr2)

	elif (m2 < m1 and len1 > 2 and len2 > 2):

		if (len1%2) != 0:
			mid1 = mid1 + 1

		arr1 = arr1[:mid1]
		arr2 = arr2[mid2:]
		return median_binary_search(arr1,arr2)



 #arr1 = [10,15,20,25,30,35,37,40]
# arr1 = [1,3,5,7,9,11,13,17,40,100]
# arr2 = [6,8,10,12,14,16,18,20,60,90]

# arr1 = [1,3,5,7,9,11,30]
# arr2 = [15,30,40,50,60,70,80]

arr1 = [6, 8, 12, 13,18, 20]
arr2 = [3, 7, 9, 13, 15, 22]

_median = median_binary_search(arr1,arr2)
print "The median of the merged array is:", _median

