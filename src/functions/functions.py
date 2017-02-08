# Created by labattula on 30/12/15.

def main():
    callfunction()
    printfunc()


def callfunction():
    print("in the function")
    functionWithArg()


def functionWithArg(arg=None):
    print('the value is..', arg)


def printfunc():
    try:
        for n in inclusive_range(0,25,5):
            print(n,end=' ')
    except TypeError as e:
        print(e)

def rangeFunc():
    return range(25)

def inclusive_range(*args):
    numargs = len(args)
    if numargs<1 : raise TypeError('requires at least one argument')
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        (start,stop) = args
        step = 1
    elif numargs == 3:
        (start,stop,step) = args
    else:
        raise TypeError("expected 3 argumnets, but got {} arguments".format(numargs))

    i = start
    while i<=stop:
        yield i
        i += step

if __name__ == '__main__':
    main()
