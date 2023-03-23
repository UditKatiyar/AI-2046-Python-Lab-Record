# creating accumulator function 
def intpicker():
        x=int(input("Please pick a positive integer"))
        sum=0
        if x >= 0:
            for i in range(1,x):
                sum=sum+i
            print(sum)
            return intpicker()
        else:
            return intpicker()