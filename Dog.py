# creating classes

# methods are operations that can be performed by the object
# self variable is used to visibly, automatically pass the Dog objects that are created into the methods
class Dog:

    # instantiates object within object itself
    # any time an arg is passed into Dog(), it will pass to this method
    # usually pass required 'attributes' (essentially, these attributes are instance variables)
    def __init__(self, name, age):
        # created an attribute of the class Dog
        # attribute is stored permanently for that object
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def treat(self, x):
        return(x+1)

    def bark(self):
        print('bark')

# instantiating (creating a new instance) a new object of type Dog()
d = Dog('Lola', 3)
print(d.get_name(), d.get_age())
d2 = Dog('Bodie', 1)
print(d2.get_name(), d2.get_age())

# Dog object can call Dog methods
d.bark()

# says 'class __main__.Dog' 
print(type(d))