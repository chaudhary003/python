def kangaroo(x1, v1, x2, v2):
	if not((0<=x1<10**4)and (x1<x2<10**4)and (1<=v1<10**4)and(1<=v2<10**4)):
		return "NO"
	if(x1<x2)and(v1<v2):
		return "NO"
	if ((v1 !=v2)and (x2-x1)%(v1-v2)==0):
		return "YES"
	else:
		return "NO"