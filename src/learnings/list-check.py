# Created by labattula on 29/12/15.

def main():
    print("this is main function")

    tup = (2,4,6,8) # tuples are immutable
    print(type(tup),tup)

    strList = ("lakshman","check","print")
    print(type(strList),strList)

    list = [1,3,5,4,6]
    list.append(80)
    list.insert(0,30)
    list.insert(2,8)
    print(type(list),list)

    string = 'lakshman'
    for i in string:
        print(i,end=' ')


if __name__ == '__main__':
    main()