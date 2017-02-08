# Created by labattula on 04/01/16.

class Duck:
    def __init__(self, **kwargs):
        print("in the constructor")
        self._properties = kwargs

    def set_properties(self, key, value):
        self._properties[key] = value

    def get_properties(self, key):
        return self._properties.get(key, None)

    def quack(self):
        print('quacking')

    def walk(self):
        print("walking")

    @property
    def color(self):
        return self._properties.get('color', None)

    @color.setter
    def color(self, c):
        self._properties['color'] = c

    @color.deleter
    def color(self):
        del self._properties['color']


def main():
    donald = Duck()
    donald.color = 'white'
    print('{} color'.format(donald.color))
    print()


if __name__ == '__main__':
    main()
