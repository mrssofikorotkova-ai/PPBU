r = input()
c = int(r[r.index(' ')+1:])
r = int(r[:r.index(' ')])
for i in range(r):
    i = i+1
    if i == 1 or i == r:
        print('#' * c)
    else:
        for y in range(c):
            y = y+1
            if y == 1 or y == c:
                print('#',end='')
            elif y == i:
                print('*',end='')
            elif (y+i)%2 == 0:
                print(".",end='')
            else:
                print(':', end='')
        print()