# Python Program to Check Prime Number.
num = float(input(" enter the number u want to check:"))
if num > 1:
    for i in range(2,int(num/2)+1):
        if (num % i == 0):
            print(num, "is not a Prime Number")
            break
    else:
        print(num,"is a Prime number")