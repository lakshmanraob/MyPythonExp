# Created by labattula on 29/12/15.

def main():
    print("this is dictionary file")
    d = dict(
        one=1,two=2,three=3,four=4,five='five'
    )

    d['six'] = 6
    for k in sorted(d.keys()):
        print(k,d[k])

    print('--retrieving the value from dict--')
    va = 'seven'
    print(d.get(va,'other'))

    for index, val in enumerate(d):
        print(index,val)

if __name__ == '__main__':
    main()