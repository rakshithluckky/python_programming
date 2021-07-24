#syntax:
#def functionname(parameters)
#     function_site
#     return(expression)

#example
def fun(s):
  print(s)
  return
fun("This is an example")
fun(1234)
print()

#pass by reference
def changeme(mylist):
  print("Value inside the function before changing:",mylist)
  mylist[2]=50
  print("Value inside the function after changing:",mylist)
  return
mylist=[10,20,30]
changeme(mylist)
print("Value outside the function after changing:",mylist)
print()

#pass by value
def changeme(mylist):
  mylist=[70,60,50]
  print("Value inside the function:",mylist)
  return
mylist=[10,20,30]
changeme(mylist)
print("Value outside the function:",mylist)
print()
