### Program to find k frequent elements in an array. The code requires at least k distinct element to appear more than once

## Time complexity: O(N) where N in the number of entries in the array
## Worst Space complexity: O(N)

def k_freq_elem(arr,k):

	n = len(arr)

	## Use a HashMap (python dictionary)
	val_freq = {k:0 for k in arr}

	for i in range(n):

		if arr[i] in val_freq:
			val_freq[arr[i]] = val_freq[arr[i]] + 1


	val_freq = sorted(val_freq.items(), key = lambda s: s[1])[::-1]

	lst = []

	for m in range(k):
		elem = val_freq[:k][m][0]
		lst.append(elem)

	return lst




## Driver code


# arr = [1,6,1,2,4,1,6,1]
arr = [2,3,4,5,6,7,8,9]
k = 2

lst = k_freq_elem(arr,k)
print "The top two most frequent element in the list are:", lst



