print("hello module 2")
def display():
    print("hello display from outer")
class Demo:
    def display(msg):
        print(msg)
        return
class Temp:
    def show(self,msg):
        print("hello show")
        Demo.display(msg)
class Temp2:
    def show2():
        print("hello show")

def main():
    t=Temp()
    t.show("hello main module")
    Temp2.show2()
    display()
main()
