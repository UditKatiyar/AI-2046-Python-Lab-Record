# Binary Search in python
def binary_search(arr,low,high,x):
    if high>=low:
        mid =(high+low)//2
        if arr[mid]==x:
          return mid
    
        elif arr[mid]>x:
          return binary_search(arr, low, mid -1,x)
    else:
        return binary_search(arr,low, mid+1,high,x)
    
# test array 
arr = [2,3,4,67,76,56,34]
x=68

# function call
result = binary_search(arr,0,len(arr)-1,x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

    
  