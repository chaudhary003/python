def plusMinus(arr):
    #
    # Write your code here.
    #
    n=len(arr)
    count1=0
    count2=0
    count3=0
    for element in arr:
	    if element>0:
		    count1=count1+1
    print(count1/n)
    for element in arr:
	    if element<0:
		    count2=count2+1
    print(count2/n)
    for element in arr:
	    if element==0:
		    count3=count3+1
    print(count3/n)
	
	