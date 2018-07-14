### Problem: Given an array and a number x, check for a pair in the array with sum as x
### Time complexity: O(nlogn) == heap sort
### Space complexity O(1)


def min_heapify(arr,i,n):
	l = 2*i
	r = 2*i + 1

	if (l<=n and arr[l]<arr[i]):
		smallest = l
	else:
		smallest = i

	if (r<=n and arr[r]<arr[smallest]):
		smallest = r

	if smallest != i:
		tmp = arr[i]
		arr[i] = arr[smallest]
		arr[smallest] = tmp
		min_heapify(arr,smallest,n)


def build_min_heap(arr,n):
	for i in range(n/2,-1,-1):
		min_heapify(arr,i,n)

def heap_sort(arr,n):
	while n>=0:
		build_min_heap(arr,n)
		swap = arr[0]
		arr[0] = arr[n]
		arr[n] = swap
		n = n-1
	return arr


def two_sum(arr,n,x):

	lst = []
	i = 0

	while i<n:

		tmp = arr[i] + arr[n]
		if tmp == x:
			lst.append([arr[i],arr[n]])
			i = i+1
			n = n-1
		elif tmp < x:
			n = n-1    # when using min heap. Change it to i = i+1 when using max heap
		elif tmp > x:
			i = i+1    # when using min heap. Change it to n = n-1 when using max heap

	return lst


arr = [3,2,4,1,5,7,8,6]
n = len(arr)-1
arr = heap_sort(arr,n)   # uses min heap, returns array in descending order
lst = two_sum(arr,n,8)
print (lst)
