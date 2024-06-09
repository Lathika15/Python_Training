a=int(input())
lst=[]
for i in range (0,a):
    ar=int(input())
    lst.append(ar)
l=len(lst)
temp=0
for i in range(0,l):
    for j in range (i+1,l):
        if(lst[i]>lst[j]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
print("Array sorted in ascending order = ")
for i in range(0,l):
    print(lst[i],end=" ")


            




