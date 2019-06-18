class Node:    
	def __init__(self,data=none,next=none):
	    self.data=data
        self.next= next
		
	def getData(self):
	    return self.data
		
	def getNext(self):
	    return self.next
	def setData(self,data):
	    self.data=data
	def setNext(self,next):
	    self.next=next
		

class LinkedList:
    def __init__(self,head=none):
	    self.head=head
		
    def size(self):
	    return size
		
	def is_empty():
	    if(head==none):
		    return True
		else:
		    return False
	def add_at_front(data):
	    node=Node(data)
		if (is_empty()):
		    node=head
			head=node 
		else:
		     node.next=head
			 head =node
	def add_at_end(data):
	    node=Node(data)
		if(is_empty()):
		    node=head
			head=node 
		else:
		    last=head
		    while(not last.next ==None):
			    last=last.next
			last.next=node
			node.next=None 
def main():
    lis =LinkedList()
	lis.is_empty()
if __name__=="__main__"