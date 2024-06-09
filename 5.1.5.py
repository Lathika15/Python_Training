a=int(input())
b=[]
for i in range(0,a):
    ar=float(input())
    b.append(ar)

me = 0
for x in b:
    me += x
me /= a
var = 0
for x in b:
    var += (x - me) ** 2
var /=a
std_deviation = var ** 0.5

print("Mean:{:.2f}".format(me))
print("Variance:{:.2f}".format(var))
print("Standard Deviation:{:.2f}".format(std_deviation))   
            




