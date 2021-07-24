#Random library
import random
print("Using random library")
#1)choice(seq)    2)random()    3)shuffle(list)
print("random number in the given range is ",random.choice(range(100)))
print()
print("random character in the given range is ",random.choice("hello world"))
print()
print("random number in the range 0 to 1 is ",random.random())
print()
a=[1,2,3,4,5,'w']
random.shuffle(a)
print("shuffled  list is ",a)
print()
#4)randrange([start,]stop[,step])     5)uniform()
print("random number in the given range by skipping given numbers is ",random.randrange(1,101,2))
print()
print("random in the give range is ",random.randrange(100))
print()
print("random float number in the given range is ",random.uniform(5,10))
print()
#6)random.sample(seq,len)
a="13sujhufs942-242"
print("random list of the given length from given string is:",random.sample(a,5))
