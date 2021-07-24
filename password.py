import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,_-"
all=lower+upper+numbers+symbols
print(all)
l=16
s=" "
password=s.join(random.sample(all,l))
print(password)
