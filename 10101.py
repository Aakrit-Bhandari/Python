def prime(n):
    l1 = []
    flag = 1
    for x in range(2,n):
        if n%x==0:
            flag=0
            break
    if flag==1:
        return 1
    else:
        return 0 
li = [prime(x) for x in  range (2,12)]
print(li)


