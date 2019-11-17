
n = int(input("Enter the value of n: "))
def fun(n):
    for i in range(1,n):
        if(i%5==0) and (i%7==0):
            yield i
            
    

print(list(fun(n)))

