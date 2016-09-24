def insertionSort(array):
	for i in range(len(array)):
		temp = array[i]
		
		for j in range(i,-1,-1):
			if array[j]<array[j-1] and j>0:
				array[j] = array[j-1]
				array[j-1] = temp
				
				
				
a = [12,4,12,8,13,5,4,67,9,3,3,5,2,2]
insertionSort(a)
print a