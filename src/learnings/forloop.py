
# fh = open("lines.txt")
# for line in fh.readlines():
#    print(line,end='')


def isPrime(n):
    if n == 1:
        print("1 is special")
        return False
    
    for x in range(2, n):
        if n % x == 0:
            print('{} is equals to {} X {} '.format(n, x, n // x))
            return False
    else:
        print('{} is a prime number'.format(n))
        return True

    s = 'this is a String'

    for index,t in enumerate(s):
        if t == 'S': print('index {} is S'.format(index))
        elif t == 's': print('index {} is s'.format(index))
     
for t in range(1, 20):
    isPrime(t)
