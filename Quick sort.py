def quickSort(array,first,last):
	#Sort the array elements array[first] through array[last]
	
	if first< last :
		pivotIndex = partition(array,first,last)
		
		quickSort(array,first,pivotIndex-1)
		quickSort(array,pivotIndex+1,last)
	
		
def partition(array,first,last):
	a = array[first]

	lb = first
	ub = last
	down = lb
	up = ub
	
	while up > down:
		while (not (array[down] > a)) and down < len(array)-1:
			down += 1
		while not (array[up] <= a):
			up -= 1
		if up > down:
			temp = array[down]
			array[down] = array[up]
			array[up] = temp
		
	temp = array[up]
	array[up] = array[lb]
	array[lb] = temp
	
	return up
	
	
	

a = [12,4,12,13,55,67,9,3,3,5,2,2]
quickSort(a,0,len(a)-1)
print a