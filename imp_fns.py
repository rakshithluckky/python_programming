#Map function example:
#map(fn,*iteration or seq)
#Python program to convert a list of integers and a tuple of integers into a list of strings:
print("Example of map function:")
nums_list=[1,2,3,4]
nums_tuple=(0,1,2,3)
print("original list and tuple:")
print(nums_list)
print(nums_tuple)
result_list=list(map(str,nums_list))
result_tuple=tuple(map(str,nums_tuple))
print("result list and tuple:")
print(result_list)
print(result_tuple)
print()

#Lambda function example:
#example 1:
a=lambda x,y:x+y
print("Using lambda function:",a(10,20))
print()
#Example 2:
var=lambda a,b:a if a>b else b
print("Using lambda function 2:",var(10,2))
print()
