def is_sublist(sublist,superlist):
	if(is_empty(superlist)):
		return False
	elif(is_empty(sublist)):
		return True
	elif(len(sublist)>len(superlist)):
		return False
	else:
		for i in range(len(superlist)):
			if(superlist[i]==sublist[0]):
				n=1
				while(n<len(sublist)and superlist[i+n]==sublist[n]):
					n=n+1

				if n==len(sublist):
					return True
		return False

	
	
def is_empty(lis):
	if(len(lis)<=0):
		return True
	return False
	
	
def member(x,l):
	for var in l:
		if var==x:
			return True
	else:
		return False
		
def is_subset(sub,sup):
	for var in sub:
		if(not(member(var,sup))):
			return False
	else:
		return True