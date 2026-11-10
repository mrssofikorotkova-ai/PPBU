
time1 = input()
time2 = input()
h1 = int(time1[0:2])
m1 = int(time1[3:5])
h2 = int(time2[0:2])
m2 = int(time2[3:5])

if not (len(time1) == 5 and time1[2]==':' and 0<=h1<=23 and 0<=m1<=59):
 print('Формат времени неверный')
elif not (len(time2) == 5 and time2[2] == ':' and 0 <= h2 <= 23 and 0 <= m2 <= 59):
 print('Формат времени неверный')
else:
 x = int()
 y = int()
 now = int(h1*60+m1)
 alarm = int(time2[0:2])*60+int(time2[3:5])
 if now == alarm:
  x = 0
  y = 0
 elif (alarm-now)<0:
  x = (alarm-now)%1440//60
  y = (alarm - now)%1440%60
 else:
  x = (alarm-now)//60
  y = (alarm-now)%60
 print(f'Через {x} ч и {y} мин')

