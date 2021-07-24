#if else looping
a=eval(input("Enter number: "))
if a%2==0:
  print("even number")
else:
  print("odd number")
print("          ")
print(" ")

#if elif else looping
a=eval(input("Enter number: "))
if a<0:
    print("-ve number")
elif a==0:
    print("zero")
else:
    print("+ve number")
print(" ")
print(" ")

#nested if looping
a=eval(input("Enter age: "))
if a>=12:
  print("Eligible to watch the match")
  if a<=20:
    print("Ticket price is Rs.1000 ")
  else:
    print("Ticket price is Rs.1200 ")
else:
  print("Not Eligible to watch the match")
print("")
