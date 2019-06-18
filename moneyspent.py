def getMoneySpent(budget,no_key, no_usb,key,usb):
	if not(1<=budget<=10**6):
		return "invalid input"
	if not((1<=no_key<=10**2)and (1<=no_usb<=10**2)):
		return "invaild"
	if not((no_key==len(key))and(no_usb==len(usb))):
		return "invalid data"
	lis=[]
	for element in key:
		for u in usb:
			lis.append(u+element)
	release={}
	for item in lis:
		release[budget-item]=item
	print(release)
	lis=[]
	lis=list(release.keys())
	print(lis)
	for i in lis:
		if i<0:
			lis.remove(i)
	minkey=(min(lis))
	print(minkey)
	print(release.get(minkey))