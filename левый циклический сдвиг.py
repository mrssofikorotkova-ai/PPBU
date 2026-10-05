""""левый циклический сдвиг"""
l = [22,33,44,55,99]
temp = l[0]
n = len(l)
for i in range(n-1):
    l[i] = l[i+1]
l[-1] = temp
print(l)
temp = l.pop(0)
l.append(temp)
print(l)

x = 10
y = 15
print(x,y)

x,y,z = y,x,x
print(x,y,z)