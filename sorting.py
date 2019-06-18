def bubbleSort(lis):
	for i in range(len(lis)):
		for k in range(len(lis)-1,i,-1):
			if lis[k]<=lis[k-1]:
				swap(lis,k,k-1)
def swap(lis,x,y):
	temp=lis[x]
	lis[x]=lis[y]
	lis[y]=temp
	
def selectionSort(lis):
	for i in range(len(lis)):
		least=i
		for k in range(i+1,len(lis)):
			if lis[least]>lis[k]:
				least=k
		lis[i],lis[least]=lis[least],lis[i]

def insertionSort(lis):
	for i in range(1, len(lis)):
		temp=lis[i]
		j=i
		while(j>0 and temp<lis[j-1]):
			lis[j]=lis[j-1]
			j-=1
		lis[j]=temp


def mergeSort(lis):
    if len(lis)>1:
        mid=len(lis)//2
        Lhalf=lis[:mid]
        Rhalf=lis[mid:]
        mergeSort(Lhalf)
        mergeSort(Rhalf)
        i=j=k=0
        while i<len(Lhalf)and j<len(Rhalf):
            if Lhalf[i]<Rhalf[j]
