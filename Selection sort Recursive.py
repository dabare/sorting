def selectionSort(array,first,last):
	#Sort the array elements array[first] through array[last] recursively
	
	if first>=last :
		return
	
	indexOfNextSmallest = first
	smallest = array[first]
	
	for i in range(first+1,last+1):
		if smallest>array[i] :
			indexOfNextSmallest = i
			smallest = array[i]
			
	array[indexOfNextSmallest] = array[first]
	array[first]=smallest
	
	selectionSort(array,first+1,last)
	
	
a = [12,4,12,8,13,5,4,67,9,3,3,5,2,2]

selectionSort(a,0,len(a)-1)
print a