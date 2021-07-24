#Single Inheritance
#Example 1
class Teacher:
    def display(self):
        print("This is class teacher")

class Student(Teacher):
    def show(self):
        Teacher.display(self)
        print("This is class student")

obj=Student()
obj.show()
print()

#Example 2
class Parent:
    def method(self,name,age):
        self.n=name
        self.a=age
    def show(self):
        print(self.n,self.a)

class Child(Parent):
    def method2(self,name,age,gender):
        Parent.method(self,name,age)#method1 for inheritance
        self.g=gender
    def show2(self):
        self.show()#method2 for inheritance
        print(self.g)

o=Child()
o.method2("abc",13,"m")
o.show2()
print()

#Example 3
class Employee:
    def __init__(self,ecode,ename,salary):
        self.ecode=ecode
        self.ename=ename
        self.salary=salary
    def putdata(self):
        print("Code=",self.ecode,"\nName=",self.ename,"\nSalary=",self.salary)
class Salesman(Employee):
    def __init__(self,ecode,ename,salary,dept):
        Employee.__init__(self,ecode,ename,salary)
        self.d=dept
    def printdata(self):
        self.putdata()
        print("Department=",self.d)
s=Salesman(10001,"ABC","1000Cr","ZXC")
s.printdata()
