#String's in built-in function:
#1)capitalize()      2)center(a,b)
x="rakshith"
print("x=",x)
print("capitalized x is ",x.capitalize())
print()
x="rakshith"
b="*"
print("string after centering is ",x.center(20,b))
print()
#3)count()    4)find
print("no.of characters is ",x.count("h"))
print()
print("no.of characters in the given range",x.count("r",3,10))
print()
print("place of given character is ",x.find("i"))
print()
print("place of given character in the given range is ",x.find("i",0,3))
print()
#5)endswith()  booleanoutput    #6)join()
print("does the string ends with given character?:",x.endswith("h"))
print()
print("does the string ends with given character in the given range?:",x.endswith("h",1,4))
print()
s='-'
seq=['1','2','a']
print(s.join(seq))
print()
#7)isalnum()     #8)isalpha()      both  giveboolean output
y="2345"
print("y=",y)
print("is the given string contains all number or not",y.isalnum())
print()
print("is the given string contains all number or not",y.isalpha())
print()
print()

#Lists built-in functions:
#max(),min(),count() are same
#1)extend()   2)sort()    3)sorted()
list1=['add','sdffdsf','fwdfsfs','ewredsf','geargf']
list2=[3,234,2344.24,4534758]
list1.sort()
print("sorting list1 in ascending order:",list1)
print()
list1.sort(reverse=True)
print("sorting list1 in descending order:",list1)
print()
print("using sorted creates new list")
print(sorted(list1))
print()
list1.extend(list2)
print("list1 after extending",list1)
print()
print()

#Dictionaries built-in functions:
#1)copy()     2)get()
dict1={'c':3,'a':1,'e':5,'b':2,'d':4}
dict2=dict1.copy()
print("using copy dict1=dict2=",dict2)
print()
print("using get ",dict1.get("e"))
print()
print("using get ",dict1.get("f","none"))
print()
#3)update()  4)sorted()
x={"f":6,"g":7}
dict1.update(x)
print("after updating:",dict1)
print()
a=sorted(dict1)
print("sorting dict1 using sorted(no items):",a)
print()
a=sorted(dict1.items())
print("sorting dict1 using sorted(items):",a)
