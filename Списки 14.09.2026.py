"""list   Список"""
"""     0  1  2  3  4   """
#num = [22,33,44,55,99]
"""   -5 -4  -3  -2 -1   """
#print(num[0])
##print(num[2])
##print(num[1:-2])
##print(num[:])
##print(num[::2])
##print(num[2:])
##print(num[2::-1])
##print(num[::-1])

#nn = num
#nn = num[:]

#print(num, id(num))
#print(nn, id(nn))
#print(nn is num)
#num = [1,2,[32,4]]
#nn = num.copy()
#num[1] = 3333
#num[-1][1] = 400
#print(num,id(num))
#print(nn,id(nn))
#num = [22,100,44,100,99]
#n = num.pop()
#nn = num.pop(0)

#print(n,nn)
#print(num)
#num.remove(44)
#print(num)


num = [22,33,44,55,99,11]
#nmn = [1,2,3,4,5]
#for i in range(len(num)):
   # print(i, num[i], end  = '  ')
#print()

#for i in num:
   # print(i,end = '  ')
#print()

#cnt = 0
#for i in num:
  #  print(cnt, i, end = '  ')
  #  cnt += 1
#print()

#for r, i in enumerate(num):
 #   print( r, i, end = '  ')
#print()

#p = (22,33,44,99)
#k,*i,z = 7,5,9,10,1,32,56,100
#print(k,i,z, type(k))

names = ['Даша', "Маша",'Саша','Глаша']
names.sort()
for k,i in enumerate(names,1):
    print(f'{k}.{i}')

for k,i in zip(names,num):
    print(k,i)