array = []
n = int(input("Enter the number of elements you want to store: "))
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    array.append(element)

print("Elements in the array:")
for element in array:
    print(element)

