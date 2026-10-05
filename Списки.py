lst = [(22,'sd'),(33,'4324'),(4,'rw')]
dd = dict(lst)
print(dd)

lst = [11,22,33]
dd = dict.fromkeys(lst,100)
print(dd)

dd = {i: i**2 for i }