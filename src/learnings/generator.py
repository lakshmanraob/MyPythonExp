def isPrime(n):
    if n == 1:
        return False;  # 1 is not a prime

    for x in range(2, n):
        if n % x == 0:
            return False  # found a divisor, not a prime

    else:
        return True  # no divisor found, so prime


def primes(n=1):
    while (True):
        if isPrime(n): yield n  # yield will make a generator
        n += 1;


for n in primes():  # will generate the prime numbers
    if n > 100: break  # need prime numbers below 100
    print(n)
