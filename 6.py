num = int(input(" enter the number you want to check:"))
a= str(num)
b=a[::-1]
if a==b :
    print(" it is a palindrom")
else:
    print("not a palindrom")