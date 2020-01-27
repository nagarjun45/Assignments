def Reverselter(lis):
    reverse = list()
    for i in reversed(lis):
        reverse.append(i)
    return reverse
lis=[1,2,3,4,5,6,7,8,9,10]
print(Reverselter(lis))