a=int(input())
b=[]
for i in range(1,a+1):
    
    c=int(input())
    b.append(c)
    print(f"Enter·element·{i}:",c)
small=b[1]
large=b[1]
for i in range(0,a):
    
    if(b[i]<small):
        small=b[i]
    if(b[i]>large):
        large=b[i]
print("Largest·element:",large)
print("Smallest element:",small)
        


