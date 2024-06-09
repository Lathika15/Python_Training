num=int(input())
a=[]
c=0
if(num<=0):
    print("Invalid input")
else:
    for i in range (0,num):
        x=int(input())
        a.append(x)

for i in range(0,num):
    for j in range(i+1,num):
        if(a[i]==a[j]):
            c=c+1
if(c==0):
    print("Array elements are not repeted")
else:
    print("The repetitive element : ")
    for i in range(0,num):
        for j in range(i+1,num):
             if(a[i]==a[j]):
                 print(a[j])



            





