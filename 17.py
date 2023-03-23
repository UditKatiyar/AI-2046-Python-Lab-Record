# Use reduce function and add two number.
from functools import reduce
nums= [1,2,3,4,5,6,7,78,9,10]
result=reduce(lambda x,y:x+y,nums)
print(result)