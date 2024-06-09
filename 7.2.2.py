num=int(input())
b=0
d=0
l=len(num)
if(l<=1):
    print("Compressed string: ",num)
for i in range (len(num)):
    c=1
    while(i<l-1 and num[i]==num[i+1]):
        c+c+1
        i=i+1
    num[b+=1]=num[i]
    if (b>1):
        e=c+'0'
        num[b+=1]=e
num[b]='\0'
print("Compressed string: ",num)


