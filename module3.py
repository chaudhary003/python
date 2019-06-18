#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     19/11/2017
# Copyright:   (c) User 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)
def main():
    s=Student("arvind",100)
    #s.display()

if __name__ == '__main__':
    #main()