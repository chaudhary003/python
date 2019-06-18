def bubbleSort(lis):
	''' this is bubble sort, it works by iterating list from starting to end,
            comparing each pair of elements and swapping them if needed
            compelexity: O(n^2) in all the cases
        '''
	for i in range(len(lis)):
		for k in range(i,len(lis)-1,1):
			if lis[k]>lis[k+1]:
				swap(lis,k,k+1)

def swap(lis,x,y):
	if lis[x]>lis[y]:
		temp=lis[x]
		lis[x]=lis[y]
		lis[y]=temp




