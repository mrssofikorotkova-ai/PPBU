n = int(input())
nn = n
sm = 0
cnt = 0
while n>0:
    rem = n%10
    sm += rem
    cnt += 1
    n //= 10
print (f'В числе "{nn}" {cnt} ц. суммой {sm}')
