def timeConversion(time):
	t=time.split(":")
	#print(t)
	hh=int(t[0])
	mm=int(t[1])
	ss=t[2]
	ss=ss[0:2]
	ss=int(ss)
	#print(hh,mm,ss)
	if not((1<=hh<=12)and (00<=ss)and(ss<=59)):
		return "invalid input"
	if ("PM" in time) and (hh !=12):
		hh=hh+12
	if ("AM" in time) and (hh==12):
		hh=00
	if(0<=hh<=9):
		hh="0"+str(hh)
	if(0<=mm<=9):
		mm="0"+str(mm)
	if(0<=ss<=9):
		ss="0"+str(ss)
	hh=str(hh)
	mm=str(mm)
	ss=str(ss)
	time=":".join([hh,mm,ss])
	print(time)
	return time
