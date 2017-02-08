# Created by labattula on 04/01/16.

class Animal:
    def quack(self):
        print('animal quack')

    def walk(self):
        print('animal walk')

    def swim(self):
        print('animal swim')


class Duck(Animal):
    def __init__(self):
        print("in the constructor")

    def quack(self):
        print('quacking')

    def walk(self):
        print('walking')


class Dog(Animal):
    def swim(self):
        print('dog swimming')

    def walk(self):
        print('dog walking')


def in_forest(dog):
    dog.walk()
    dog.swim()


def in_pond(d):
    d.walk()


def main():
    dog = Dog()
    donald = Duck()

    for o in (dog, donald):
        in_forest(o)
        in_pond(o)


if __name__ == '__main__':
    main()
