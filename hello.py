import sys
import math
def main():
    print("hello main:")
    print(sys.platform)
    print("__pychache__")
    x=3+4j;
    print(type(x))
print("hello python!")
print(9**2)
def add(i,j):
    k=i+j
    print(k)
    return(k)
add(10,90)
main()
#show()
def show():
    print("this is show function")
    x="spam!"
    print("spam "*6)
    s=input()
    print(int(s))

if __name__=="__main__":
    #show()
    main()
   # add(10,90)
