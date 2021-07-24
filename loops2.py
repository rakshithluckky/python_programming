#nested looping using for looping
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k,end=" ")
    print()
print("            ")
print("            ")


#break statement example
for i in "python":
    if i=='h':
        break
    print("current letter:",i)
print("            ")
print("            ")


#continue statement example
for i in "python":
    if i=="h":
        continue
    print("current letter:",i)
print("            ")
print("            ")


#pass statement example(not used more)
for i in "python":
    if i=="h":
        pass
        print("this is pass break")
    print("current letter:",i)
print("            ")
print("            ")
