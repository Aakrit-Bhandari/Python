t = int(input("Enter the number of rows:"))
n = t
li= []
sum = []
s= 0
for i in range(0,t):
    li1=[int(x)for x in input().split()]
    li.append(li1)
    a =[s for x in li1]
    sum.append(a)
print(li)
print(sum)

