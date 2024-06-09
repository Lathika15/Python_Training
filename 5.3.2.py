a=int(input())
lst=[]
for i in range (0,a):
    c=int(input())
    lst.append(c)
print("The elements of array:")
for i in range(0,a):
    print(lst[i],end=" ")
a = len(lst)
b = 2**a
print("Total number of subsets:", b)

