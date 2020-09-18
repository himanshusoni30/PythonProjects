'''Merge Sort in arrays (list)'''

def sortArray(arr):
	l=len(arr)
	mid=l//2

	left=list()
	for i in range(0,mid):
		left.append(arr[i])
	right=list()
	for i in range(mid,l):
		right.append(arr[i])

	if l<2:
		return None
	else:
		for i in range(0,mid-1):
			left[i] = arr[i]
		for j in range(0,l-mid):
			right[j] = arr[mid+j]
	sortArray(left)	
	sortArray(right)
	mergeSortedArray(left,right,arr)

def mergeSortedArray(left,right,arr):
	nl = len(left)
	rl = len(right)
	i=0
	j=0
	k=0
	while i < nl and j < rl:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i+=1
		else:
			arr[k] = right[j]
			j+=1
		k+=1
	while i < nl:
		arr[k]=left[i]
		i+=1
		k+=1
	while j < rl:
		arr[k]=right[j]
		j+=1
		k+=1
	# return arr

def printSortedArray(arr):
	print(arr)

arr = [17, 25, 31, 13, 2, 32, 65, 100, 2000, 15, 60, 26]
print("Array before sorting: ")
print(arr)	
sortArray(arr)
print("Array after sorting in ascending order: ")
printSortedArray(arr)
# sortDescending(arr)
# print("Array after sorting in descending order: ")
# printSortedArray(arr)