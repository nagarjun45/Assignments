# print("Enter the size of the array")
# n = int(input())
# arr = []
# for i in range(n):
#     num = int(input("Number :" ))
#     arr.append(num)
def binarysearch(arr,key): 
    SortArray =  sorted(arr)
    start = 0
    end = len(SortArray) - 1
    mid = int((start+end)/2)
    while (start<=end):
        if(key==arr[mid]):
            print("Key found at :",mid+1)
            break
        elif arr[mid] > key:
            mid = mid-1
        else:
            mid = mid+1
    return mid+1

        
        
    
