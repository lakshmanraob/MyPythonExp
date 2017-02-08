
try:
    fh = open("lines.txt")
    for l in fh.readlines():
        print(l,end='')
except IOError as e:
    print("some exception {}".format(e))

print("After badness")