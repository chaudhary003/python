#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     18/11/2017
# Copyright:   (c) User 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
import test
def main():
    #for i in (1,2,3,4,5):
        #print("hello python")
        #print(i)
        input()
       # a=10;b=20
       # while a < b:
           # print(a,end=" ")
           # a=a*10
       # x="message"
       # while x:
           # print(x,end=" ")
           # x=x[1:]
pass
def squart_root(x):
    if(x<0):
       x= abs(x)
       result= x**.5
       return result
    else:
        result =x**.5
        return result

def tupledemo():
    s1="arvind",1987,9818018237,'delhi'
    #(name,age,phone_num)=s1
    print(s1)
    pass
def ar_c(r):
    c=2*math.pi*r
    a=math.pi*r**2
    return(c,a)
def listDemo():
    ls1=["hello",10.90,["python","list"],"hello again"]
    for target in ls1:
     print(target,end=" ")
    if "pyhton"  in ls1:
        print("true")

if __name__ == '__main__':
    pass
    main()
    #print(squart_root(-100))
   # tupledemo()
   # print(ar_c(10))
    listDemo()

