tp = (22,33,44,99)
k,i,*z = 7,5,9,10,1,32,56,100,
print(k,i,z)
tp = ('login','password')
print(tp,id(tp))
buf = list(tp)
buf[-1] = 'new_password'
tp = tuple(buf)
print(tp,id(tp))
