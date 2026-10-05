r = int(input()) # количество строк
c = int(input()) # количество столбцов
stk = list()
for i in range(r): ## бежим по строкам
    i = i+1
    if i == 1 or i == r:
        print('#'*c)
    else:
        for y in range(c):
            y = y + 1
            if y == 1 or y == c:
                stk.append('#')
            elif y == i:
                stk.append('*')
            elif (y+i)%2 == 0:
                stk.append('..')
            else:
                stk.append(':.')
        print(stk)


