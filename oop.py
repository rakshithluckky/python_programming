#OOP
print("OOP:")
#Format:
class Example:
    def fun(self):
        print("This is OOP")
object=Example()
print("object type is",type(object))
print("Using 1st format")
Example.fun(object)
print("Using 2nd format")
object.fun()
print()

#Example:
class Rectangle:
    def getdata(self,l,b):
        self.length=l
        self.breadth=b
        print("length and breadth of rectangle are:",self.length,",",self.breadth)
    def show(self):
        print("area of rectangle:",self.length*self.breadth)

x=3
y=5
obj=Rectangle()
obj2=Rectangle()
obj.getdata(x,y)
obj.show()
obj2.getdata(1,3)
obj2.show()
print()

#Constructor
class Const:
    def __init__(self,name):
        self.name=name
        print("constructor is called")
    def show(self):
        print("name is:",self.name)
o=Const("Rakshith")
o.show()
print()

#Destrutor
class Dest:
    def __init__(self):
        print("constructor is called")
    def __del__(self):
        print("destructor is called")
o=Dest()
print("before calling destructor")
del o
