# example of class methods and class instance variables

class Person:
    # class attribute/instance variable
    number_of_people = 0

    def __init__(self, name):
        self.name = name 
        # can increment the number_of_people value as Person objects are created
        Person.add_person()

    # decorator denotes method below a class method
    # these methods only act on the class itself
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person('Ari')
# print(p1.number_of_people)
p2  = Person('Tim')
# print(p2.number_of_people)
print(Person.number_of_people)

# you can change the class instance variable values outside of the class if need be
# Person.number_of_people = 8
# you can also access the instance variables using any object of the same type as the class
# print(p1.number_of_people)