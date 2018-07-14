### Python code to find the majority element in an array
### A majority element in an array A[] of size n is an element that appears more than n/2 times 
### (and hence there is at most one such element)


## Brute force
# Time Complexity: O(N*N)
# Space Complexity: O(1)

def majority_element(arr,n):
	max_count = 0
	index = -1

	for i in range(n):
		count = 0
		for j in range(n):
			if arr[i] == arr[j]:
				count = count + 1

		if (count > max_count):
			max_count = count
			index = i

	return index, max_count

arr = [3,3,4,4,4,2,4,4]
index, max_count = majority_element(arr,len(arr))
print (arr[index], max_count)

## -----------------------------------------------------------------------

## Using Python Counter object (Hashmap)

from collections import Counter


arr = [3,3,4,4,4,2,4,4]
output = Counter(arr)
 
# print (output.most_common(1))
print max(output.keys())

## -----------------------------------------------------------------------


### Using Moore's voting algorithm

### Time complexity: O(n)
### Space complexity: O(1)

def moores_voting(arr,n):

	maj_index = 0
	count = 1

	for i in range(1,n):
		if (arr[maj_index] == arr[i]):
			count = count + 1
		else:
			count = count - 1

		if count == 0:
			maj_index = i
			count = 1

	cand = arr[maj_index]

	## code to check whether cand is the majority element

	tmp_count = 0
	for i in range(n):
		if (arr[i] == cand):
			tmp_count = tmp_count + 1

	if (tmp_count > n/2):
		return cand
	else:
		return None


arr = [3,3,4,4,4,2,4,4,4,3,4]
cand = moores_voting(arr,len(arr))

print "The majority element in the array is:", cand



