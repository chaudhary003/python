#triplet comparison 
def solve(a0, a1, a2, b0, b1, b2):
    #
    # Write your code here.
    #
	A=[a0,a1,a2]
	B=[b0,b1,b2]
	for a in A:
		#print(a)
		if not(1<=a<100):
			return "invalid input"
	for b in B:
		#print(b)
		if not(1<=b<100):
			return "invalid input"
	a=(1 if a0>b0 else 0)+(1 if a1>b1 else 0)+(1 if a2>b2 else 0)
	b=(1 if a0<b0 else 0)+(1 if a1<b1 else 0)+(1 if a2<b2 else 0)
	return (a,b)