#while looping
a=1
while a<=10:
    print(a)
    a+=1
print("end")
print("            ")
print("            ")


#using else with while looping
a=0
while a<5:
    print(a," is less than 5")
    a+=1
else:
    print(a," is not less than 5")
print("            ")
print("            ")


#for looping
#example 1
for letter in "python":
    print("current letter:",letter)
print("            ")
print("            ")


#example 2
fruits=["banana","apple","mango","guava","orange"]
for i in fruits:
    print("current fruit:",i)
