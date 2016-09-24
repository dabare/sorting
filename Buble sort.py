def bubleSort(array):
	for i in range(len(array)-1):
		for j in range (len(array)-1,i,-1):
			if array[j]<array[j-1]:
				temp = array[j]
				array[j]=array[j-1]
				array[j-1]=temp


a = [12,4,12,8,13,5,4,67,9,3,3,5,2,2]
bubleSort(a)
print a