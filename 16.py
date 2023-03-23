# Double a List using map function
list1=[12,34,56,10]
print(" the original list is:"+str(list1))
output= list(map(lambda x: x + x, list1))
print("Double List is : " + str(output))