#Multi Level Inheritance Example
class Base:
    def __init__(self,name):
        self.n=name
    def getname(self):
        return self.n
class Child(Base):
    def __init__(self,name,age):
        Base.__init__(self,name)
        self.age=age
    def getage(self):
        return self.age
class Grandchild(Child):
    def __init__(self,name,age,address):
        Child.__init__(self,name,age)
        self.a=address
    def getaddress(self):
        self.getage()
        self.getname()
        return self.a

o=Grandchild("Raj",32,"Delhi")
print(o.getname(),o.getage(),o.getaddress())
print()

#Multiple Inheritance Example
class Student:
    def __init__(self,rollno,name):
        self.r=rollno
        self.n=name
    def putdata(self):
        print("Rollno=",self.r,"\nName=",self.n)
class Test:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def putmarks(self):
        print("Marks in m1=",self.m1,"\nMarks in m2=",self.m2)
class Result(Student,Test):
    def __init__(self,rollno,name,m1,m2,age):
        Student.__init__(self,rollno,name)
        Test.__init__(self,m1,m2)
        self.a=age
    def display(self):
        self.putdata()
        self.putmarks()
        print("Age=",self.a)

a=Result(1,"Raj",99,100,19)
a.display()
print()

#Heirarchical Inhritance Example
class Parent:
    def __init__(self,pname):
        self.pn=pname
    def display(self):
        print("Parent=",self.pn)
class Child1(Parent):
    def __init__(self,pname,c1name):
        self.c1n=c1name
        Parent.__init__(self,pname)
    def display2(self):
        self.display()
        print("Child1 name=",self.c1n)
class Child2(Parent):
    def __init__(self,pname,c2name):
        self.c2n=c2name
        Parent.__init__(self,pname)
    def display3(self):
        self.display()
        print("Child2 name=",self.c2n)

c1=Child1("abc","zxc")
c1.display2()
c2=Child2("abc","qwe")
c2.display3()
