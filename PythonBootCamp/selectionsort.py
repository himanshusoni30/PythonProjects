'''Selection Sort in arrays (list)'''

def sortAscending(arr):
	for i in range(0,len(arr)-1):
		for j in range(i,len(arr)):
			if arr[i] > arr[j]:
				arr[i] = arr[i] + arr[j]
				arr[j] = arr[i] - arr[j]
				arr[i] = arr[i] - arr[j]
	# return arr

def sortDescending(arr):
	for i in range(0,len(arr)-1):
		for j in range(i,len(arr)):
			if arr[i] < arr[j]:
				arr[i] = arr[i] + arr[j]
				arr[j] = arr[i] - arr[j]
				arr[i] = arr[i] - arr[j]
	# return arr

def printSortedArray(arr):
	print(arr)

arr = [17, 25, 31, 13, 2, 32, 65, 100, 2000]
print("Array before sorting: ")
print(arr)	
sortAscending(arr)
print("Array after sorting in ascending order: ")
printSortedArray(arr)
sortDescending(arr)
print("Array after sorting in descending order: ")
printSortedArray(arr)