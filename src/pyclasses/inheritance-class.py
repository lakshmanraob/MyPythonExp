# Created by labattula on 04/01/16.

class Animal:
    def walk(self):
        print('hey i am walkinig')

    def eat(self):
        print('hey i can eat as well')

    def talk(self):
        print('hey i can talk as well')


class Duck(Animal):
    def __init__(self):
        print('in the constructor')

    def talk(self):
        print("duck is quacking")

    def walk(self):
        # super().walk() calling the super class method
        super(Duck, self).walk()
        print("duck is walking")


def main():
    donald = Duck()
    donald.walk()
    donald.talk()
    donald.eat()


if __name__ == '__main__':
    main()
