def staircase(n):
	for i in range(1,n+1):
		print(("#"*i).rjust(n," "))
		
def staircase2(n):
    for i in range(1,n+1):
		print(("#"*i).ljust(n," "))
