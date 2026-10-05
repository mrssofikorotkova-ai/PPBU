from encodings import kz1048
from math import *

n = int(input()) #четырёхзначный код
num4 = n%10
num3 = n//10%10
num2 = n//100%10
num1 = n//1000%10

k1 = int()
k =int()
k2 = int()
for i in range(9):
    if i!=(num1,num2,num3,num4):
        k = i
    if i!=k:
        k1 = i
    if i!=k1:
        k2 = i
    print(k, k1, k2)

num1 != num2 != num3 != num4

