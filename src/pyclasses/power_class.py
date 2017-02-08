# Created by labattula on 04/01/16.

class powerDuck:
    def __init__(self, **kwargs):
        self._variables = kwargs
        print('in the constructor')

    def quack(self):
        print('{} duck is quacking'.format(self.get_variable('color')))
        if self.get_variable('feet') > 0:
            print('duck is having {} feet'.format(self.get_variable('feet')))


    def walk(self):
        print('{} duck is walking'.format(self.get_variable('color')))

    def set_variable(self, key, value):
        self._variables[key] = value

    def get_variable(self, key):
        return self._variables.get(key, None)


def main():
    powDuck = powerDuck(feet=2,color='white')
    powDuck.get_variable('feet')
    powDuck.quack()


if __name__ == '__main__':
    main()
