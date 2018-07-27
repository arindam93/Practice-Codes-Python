# Given a set of numbers in an array, 
# First element represents the height of the east most building 
# and next is the building to the west of it and so on. 
# Print the list of buildings that have a 
# sunset view. If a building is shorter than another building 
# to its west then it looses its sunset view.


def sunset_buildings(arr):

	n = len(arr)
	sunset_bldg = []

	for i in range(n-1):
		if arr[i] > arr[i+1]:
			sunset_bldg.append(arr[i])


	sunset_bldg.append(arr[-1])

	return sunset_bldg[::-1]


arr = [9,4,6,8,1,5,1,2,3,2]
sunset_bldgs = sunset_buildings(arr)
print sunset_bldgs

