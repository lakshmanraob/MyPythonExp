# Created by labattula on 30/12/15.
import os

def main():
    print("main function")

    s = 'this is a String'

    # break, continue and else
    for c in s:
        if c == ' ': continue # just continue to the next iteration with out executing the next statement
        print(c,end='')
    else:
        print(' else')

    print("After for loop")
    # break will stop the execution of the for loop and move to next statement

    print(os.environ['PATH'])

    print("---Printing the environment variables-----")
    for val in os.environ:
        print(val,'=',os.environ.get(val))
    print("---Printing the environment variables-----")

if __name__ == '__main__':
    main()