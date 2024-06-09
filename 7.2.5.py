s1=input()
lst=list(s1)
a=len(lst)
temp=0
for i in range(0,a):
    for j in range (i+1,a):
        if(lst[i]>lst[j]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
b=''.join(lst)
print("The output string : ",b)
