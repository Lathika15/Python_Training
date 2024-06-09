s = input("Enter the string: ")
n = int(input("Enter the number: "))
a = {}
for i in s:
    a[i] = a.get(i, 0) + 1
b = ""
for i in sorted(a, key=a.get, reverse=True):
    if a[i] >= n:
        b += char * n
print(b)





