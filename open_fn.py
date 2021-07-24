#open function

#reading from file
f=open("test.txt",mode='r')
print(f.read())

#reading line by line
f=open("test.txt","r")
print(f.readline())
print(f.readline())

#reading as loop
f=open("test.txt","r")
for x in f:
    print(x)

#writing to file
f=open("test1.txt","w")
f.write("writing in new file")
#f.close()
f=open("test1.txt",mode='r')
print(f.read())
#f.close()

#appending to file
f=open("test2.txt","a+")
f.write(" appending")
#f.close()
f=open("test2.txt",mode='r')
print(f.read())
#f.close()
