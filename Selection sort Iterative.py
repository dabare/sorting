def selectionSort(array,n):
	#Sort the first n elements of the given array
	for i in range(n-1):
		indexOfNextSmallest = i
		smallest = array[i]
		
		for j in range(i+1,n):
			if smallest>array[j] :
				indexOfNextSmallest = j
				smallest = array[j]
			
		array[indexOfNextSmallest] = array[i]
		array[i]=smallest
	
	
	
a = [12,4,12,13,55,67,9,3,3,5,2,2]

selectionSort(a,len(a))
print a