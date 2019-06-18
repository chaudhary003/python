import overloading
class OOpsDemo:
    @overload
    def show(self,x):
	    print(x)
    @overload		
    def show(self,x,y):
        print(x,y)
		
Oop= OOpsDemo()
Oop.show(120)