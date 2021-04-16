# another example for inheritance

# Pet is the superclass and carries all the common attributes of the subclasses
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'My name is {self.name} and I am {self.age} years old')

    def speak(self):
        print('I do not know what to say')


