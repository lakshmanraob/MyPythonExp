
class AnimalActions:
    def quack(self): return self._doAction('quack')
    def bark(self): return self._doAction('bark')
    def fly(self): return self._doAction('fly')
    def bite(self): return self._doAction('bite')
    
    def _doAction(self, action):
        if action in self.strings:
            return self.animalName()+" "+self.strings[action]
        else:
            return "the {} will not {}".format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()
    

class dog(AnimalActions):
    strings = dict(
                   bark='Will bark at strangers',
                   bite='will bite'
                   )

class person(AnimalActions):
    strings = dict(
                   quack="will imitate like duck",
                   bark='will shout at others',
                   fly="will do by airplanes",
                   bite='will bite a biscuit'
                   )
    
class lion(AnimalActions):
    strings = dict(
                   bite='will bite all most all creatures',
                   bark='will roar'
                   )

class duck(AnimalActions):
    strings = dict(
                   quack='quaaaack',
                   fly='will fly a bit'
                   )
    

def in_the_forest(lion):
    print(lion.bark())
    print(lion.bite())

def at_home(person):
    print(person.bark())
    print(person.fly())
    print(person.quack())

def in_pond(duck):
    print(duck.quack())
    print(duck.fly())

def at_office(person):
    print(person.bark())
    print(person.fly())

def main():
    donald = duck()
    jhon = person()
    lionKing = lion()
    
    print("-- in the forest")
    for o in (donald, jhon, lionKing):
        in_the_forest(o)
    
    print("--at home")
    for o in (donald, jhon, lionKing):
        at_office(o)
    
    print("--in the pond")
    for o in (donald, jhon, lionKing):
        in_pond(o)
        
if __name__ == "__main__":main()