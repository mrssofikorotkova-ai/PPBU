str1 = input()
str1 = str1.split()
q1 = int(str1[0])
t1 = int(str1[1])
b1 = int(str1[2])

str2 = input()
str2 = str2.split()
q2 = int(str2[0])
t2 = int(str2[1])
b2 = int(str2[2])

if q1 > q2:
    print('FIRST')
elif q1 == q2:
    if t1 < t2:
        print('FIRST')
    elif t1 == t2:
        if b1 == b2:
            print('DRAW ')
        else:
            if b1 == 1:
                print('FIRST')
            else:
                print('SECOND')
    else:
        print('SECOND')
else:
    print('SECOND')

