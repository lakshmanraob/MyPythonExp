def main():
    a = "lakshman",
    b, c = 0, 1,
    k = (1, 3, 4, 56, 7, 89)

    print(type(a), a)
    print(b, c)
    print(k)

    for l in k:
        print(l)

    s = "less than" if b < c else "not less than"
    print(s)
    circle()

def circle(a=1):
    for i in range(a,10):
        for j in range(i):
            print(j,end=' ')
        print()

if __name__ == '__main__': main()
