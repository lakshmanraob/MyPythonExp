# Created by labattula on 04/01/16.

class inclusive_class:
    def __init__(self, *args):
        print('in the constructor')
        numargs = len(args)

        (self._start, self._step) = (0, 1)
        self._step = 1

        if numargs < 1:
            raise TypeError('expected at least one argument')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
            if self._start > self._step:
                raise TypeError("first argument {} is greater than second argument {}".format(self._start,self._stop))
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else:
            raise TypeError('expected at max 3 arguments, instead we got {}'.format(numargs))

    def __iter__(self):
        i = self._start
        while i <= self._stop:
            yield i
            i += self._step


def main():
    incl = inclusive_class(25,50,2)
    for n in incl:
        print(n, end=' ')

if __name__ == '__main__':
        main()
