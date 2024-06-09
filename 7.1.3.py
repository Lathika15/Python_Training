s=input()
a = ""
n=0
for i in range(len(s)):
    b=s[i]
    for i in range(i):
        if s[i] ==b:
            n=1
            break
    if not n:
        a=a+b
print(a)

