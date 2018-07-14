### Problem: Given an array and a number x, check for a pair in the array with sum as x
### using a hash table 
### Time complexity: O(n)
### Space complexity: O(n)


# Python program to find if there are
# two elements wtih given sum
 
# function to check for the given sum
# in the array

def two_sum(arr,n,x):

	# create an empty hash set
	s = set()

	for i in range(0,n):
		tmp = x - arr[i]
		if (tmp>=0 and tmp in s):
			print (arr[i],tmp)
		s.add(arr[i])


arr = [3,2,4,1,5,7,8,6]
n = len(arr)
two_sum(arr,n,8)
