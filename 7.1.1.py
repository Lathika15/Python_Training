s= input()
a= {}
for i in s:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
for i in a:
    print(f"{i} = {a[i]}")



            





