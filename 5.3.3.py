size = int(input("Enter array size: "))
if size <= 0:
    print("Invalid array size")
else:
    array = list(map(int, input("Enter sorted array elements: ").split()))
    a = -1
    b = None
    for i in range(size - 1):
        if array[i] == array[i + 1]:
            a = i + 1
            b = array[i]
    if a != -1:
        print("Last index:",a)
        print("Last duplicate item:",b)
    else:
        print("No duplicate found")


