class Node:
    def __init__(self,data=None,next_Node=None):
        self.data=data
        self.next_Node=next_Node
    def set_next(self,new_Next):
	    self.new_Next=new_Next
    def get_data(self):
	    return self.data
    def get_Node(self):
	    return self.next_Node
		
		
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def add(self,new_Node):
	    if self.head==None:
		    
		   
        self.head=new_Node
		
N=Node(45)
N.insert(Node(50))
#print(N)
print(N.next_Node.data)
print(N.data)
