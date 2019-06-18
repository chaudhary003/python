class BinaryTree:
	def __init__(self,data):
		self.data=data
		self.lTree=None
		self.rTree=None
	def setData(data):
		self.data=data
	def getData():
		return self.data
	def setLTree(lTree):
		self.lTree=lTree
	def getLTree():
		return self.Ltree
	def setRTree(rTree):
		self.rTree=rTree
	def getRTree():
		return self.rTree
	def insert(self,data):
		if self.data:
			if data<=self.data:
				if self.lTree==None:
					self.lTree=BinaryTree(data)
				else:
					self.lTree.insert(data)
			elif data>=self.data:
				if self.rTree==None:
					self.rTree=BinaryTree(data)
				else:
					self.rTree.insert(data)
		else:
			self.data=data
	def printTree(self):
		if self.lTree:
			self.lTree.printTree()
		print(self.data)
		if self.rTree:
			self.rTree.printTree()