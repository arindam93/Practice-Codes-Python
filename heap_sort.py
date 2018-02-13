
def max_heapify(arr,i,n):
	l = 2*i
	r = 2*i + 1

	if (l<=n and arr[l]>arr[i]):
		largest = l
	else:
		largest = i

	if (r<=n and arr[r]>arr[largest]):
		largest = r

	if largest != i:
		tmp = arr[i]
		arr[i] = arr[largest]
		arr[largest] = tmp
		max_heapify(arr,largest,n)

def build_max_heap(arr,n):

	for i in range(n/2,-1,-1):
		max_heapify(arr,i,n)

def heap_sort(arr,n):

	while n>=0:
		build_max_heap(arr,n)
		swap = arr[0]
		arr[0] = arr[n]
		arr[n] = swap
		n = n-1

# Driver code
print("Please enter some numbers: ")
str_arr = raw_input().split(' ')
arr = [int(num) for num in str_arr]

n = len(arr)-1
heap_sort(arr,n)
print("Sorted array is: ")
for k in reversed(range(len(arr))):
	print("%d" %arr[k])





