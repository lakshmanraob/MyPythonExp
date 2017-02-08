# Created by labattula on 04/01/16.

class Duck:
    def __init__(self,color='white'):
        print("constructor")
        self._color = color

    def quack(self):
        print("{} duck is quacking".format(self._color))

    def walk(self):
        print("{} duck is walking".format(self._color))

    def set_color(self,color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    donald = Duck()
    donald.quack()
    donald.set_color('Blue')
    donald.quack()
    donald.walk()

if __name__ == '__main__':
    main()
