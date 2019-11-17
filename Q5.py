print("Enter the size of the array")
n = int(input())
arr = []
for i in range(n):
    num = int(input("Number :" ))
    arr.append(num)
SortArray =  sorted(arr)
key = int(input("enter key to search in array"))
start = 0
end = n
mid = int((start+n)/2)

while (start<=end):
    if(key==arr[mid]):
        print("Key found at :",mid+1)
        break;
    elif arr[mid] > key:
        mid = mid-1
    else:
        mid = mid+1
        
        
    
