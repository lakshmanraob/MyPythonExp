class AnimalActions:
    def quack(self):
        return self.strings['quack']

    def bark(self):
        return self.strings['bark']

    def bite(self):
        return self.strings['bite']

    def fly(self):
        return self.strings['fly']


class dog(AnimalActions):
    strings = dict(
            quack="can't quacking",
            bark="more noise",
            bite="natural action",
            fly="doesn't have this capability"
    )


class duck(AnimalActions):
    strings = dict(
            quack="Quaaaack",
            bark="no action",
            bite="will bite fishes",
            fly="can try to do that"
    )


class person(AnimalActions):
    strings = dict(
            quack="can imitate duck",
            bark="can shout at others",
            bite="can bite a biscuit",
            fly="will fly in planes"
    )


class lion(AnimalActions):
    strings = dict(
            quack="not its action",
            bark="it will roar",
            bite="will eat",
            fly="no comments"
    )


def in_the_dogHouse(dog):
    print(dog.bark())
    print(dog.bite())


def at_home(person):
    print(person.fly())
    print(person.quack())


def in_forest(lion):
    print(lion.quack())
    print(lion.bark())


def main():
    donald = duck()
    jhon = person()
    lionKing = lion()

    print("--In forest")
    for o in (donald, jhon, lionKing):
        in_forest(o)

    print("--At the Home")
    at_home(lionKing)


if __name__ == "__main__": main()
