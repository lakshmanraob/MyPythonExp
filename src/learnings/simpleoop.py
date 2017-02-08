# class defininig here

class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def febSeries(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b
    
    def isPrimeFromclass(self,n):
        if n == 1:
            return False
        for x in range(2,n):
            if n % x == 0: return False
        else:
           return True
       
    def primes(self):
        n=1
        while(True):
            if self.isPrimeFromclass(n): yield n
            n += 1
    
    # primes between the range from a and b
    def primeRange(self,st,en):
        print("From ",st," to ",en," prime numbers are given below");
        for k in range(st,en):
            if self.isPrimeFromclass(k): print(k," is a prime number")
            
my = MyClass(0, 1)
for r in my.febSeries():
    if r > 100: break
    print(r,end=',')

print()
my.primeRange(10, 20)