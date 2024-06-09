a=int(input())
b=[]
c=0
for i in range(1,a+1):
    a=int(input())
    b.append(a)
search=int(input())
for i in range(0,a):
    if(b[i]==search):
        c=1
        break

if(c==1):
    print(f"{search} is found at position {i}")
else:
    print(f"{search} is not found")
        

