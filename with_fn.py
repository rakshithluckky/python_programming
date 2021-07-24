#without using with function
f=open("test1.txt","w")
f.write("writing in new file")
f=open("test1.txt",mode='r')
print(f.read())


#with using with function
with open("test1.txt","a+") as f:
    f.write(" with function")
with open("test1.txt","r") as f:
    print(f.read())
