def diagonalDifference(a):
	n=len(a)
	#if not(n==len(a)):
		#return "invalid input for n"
	for i in a:
		if not(len(i)==n):
			return "invalid input for matrix"
	for lis in a:
		for elements in lis:
			if not(-100<=elements<=100):
				return "invalid input for matrix elements"
	diff=0
	fSum=0
	sSum=0
	fsum=sum(a[i][i] for i in range(n))
	sSum=sum(a[i][n-i-1]for i in range(n))
	diff=abs(fsum-sSum)
	return diff