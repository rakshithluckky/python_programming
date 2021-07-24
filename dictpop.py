#Usage of popitem function in dictionary
shares={'Apple':100,'Google':50,'MSFT':200}
print("original shares:",shares)
returned_val=shares.popitem()
print("Shares after removing last share:",shares)
print("returned value from poping:",returned_val)
print("            ")
print("            ")



#Usage of pop function without returned value in dictionary
shares={'Apple':100,'Google':50,'MSFT':200}
print(shares)
returned_val=shares.pop('Google')
print("Shares after removing Google:",shares)
print("returned value from poping:",returned_val)
print("            ")
print("            ")


#Usage of pop function with returned value in dictionary
shares={'Apple':100,'Google':50,'MSFT':200}
print("original Shares:",shares)
returned_val=shares.pop('TCS',"Not present")
print("Shares after poping:",shares)
print("returned value from poping:",returned_val)
