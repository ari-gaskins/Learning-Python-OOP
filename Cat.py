# cat class from inheritance example

from Pet import Pet

# subclasses show the differences from superclass and other subclasses
# they require that the superclass is passed through them
class Cat(Pet):
    # if you want to add an attribute, you must slightly redefine __init__
    def __init__(self, name, age, color):
        self.color = color
        # super is in reference to the superclass Pet
        # this is intended to call the __init__ method of the superclass
        # then pass its variables
        super().__init__(name, age)

    # if the methods in the subclass carry the same name as the superclass'
    # the subclass method overrides that of the superclass
    def speak(self):
        print('Meow')

    def show(self):
        print(f'My name is {self.name}, I am {self.age} years old, and I am {self.color}')

p = Pet('April', 4)
p.speak()
p.show()
c = Cat('Mishi', 3, 'Black')
c.speak()
c.show()
