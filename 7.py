num=int(input(" enter the number whose factorial u want to find:"))
fact=1
while(num>0):
    fact= fact*num
    num=num-1
print("Factorial of the number is:")
print(fact)