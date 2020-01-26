import os
count=0
lis=[r for r, d, folder in os.walk("C://DIRECTORY")]
def func(path):
    global count
    if(os.path.isdir(lis[count++])):
        print(os.listdir(path))
        if(count==len(lis)-1):
            return 0
        else:
            count+=1
            fun(lis[count])
       
    else:
        print("directory does not exist")
        return 0
func(c://DIRECTORY)  #PASS THE FILE PATH OVER HERE