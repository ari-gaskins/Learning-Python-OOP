# dog class for inheritance example

from Pet import Pet

class Dog(Pet):
    def speak(self):
        print('Bark')

d = Dog('Lola', 3)
d.speak()
d.show()