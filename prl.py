from string import digits, ascii_letters
import random

def get_password(m):
    data = set(ascii_letters + digits) - {'0','1','o','l','I'}
    data = ''.join(data)
    data1 = ''.join(re.findall(r'[^01oLI]',ascii_letters + digits))
    password = random.sample(data1, m)
    pos = random.sample(range(m), 3)
    password[pos[0]] = password[pos[0]].lower()


    return password

def main(n, m):
    res = set()
    while len(res) < n:

