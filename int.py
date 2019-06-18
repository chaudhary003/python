def fun(p,r,n):
	return p*(1+r/100)**n,p*(1+r/100)**n-p
print(fun(1000,4,2))
