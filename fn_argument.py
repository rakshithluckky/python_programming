#Required arguments
#every parameter required or else error
def printme(a,b):
  print(a,b)
  return
printme("no","error")
print()

#keyword arguments
def printinfo(name,age):
  print("Name:",name)
  print("Age:",age)
  return
printinfo(age=19,name="Rakshith")
print()

#Default arguments
def printinfo(name,age=19):
  print("Name:",name)
  print("Age:",age)
  return
printinfo(age=20,name="Rakshith")
printinfo(name="Rakshith")
print()

#Variable-length arguments
# *indicates unkown no.of parameters
def printinfo(arg1,*vartuple):
  print(arg1)
  for var in vartuple:
    print(var)
  return
printinfo(16)
printinfo(50,60,70)
