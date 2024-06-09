a=int(input())
if(a==0):
    print("Invalid size")
else:
    lst=[]
    for i in range(0,a):
        x=int(input())
        lst.append(x)
    print("Array elements: ")
print("The unique elements found in the array are :") 
for i in range(0,a):
    n=0
    for j in range(0,a):
        if(i!=j):
            if(lst[i]==lst[j]):
                n=n+1
    if(n==0):
        print(lst[i],end=" ")

            




